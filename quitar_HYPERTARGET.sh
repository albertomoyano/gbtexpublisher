#!/bin/bash
# Asignar el primer argumento ($1) a la variable 'archivo'
archivo="$1"

# Verificar que se proporcionó un archivo como argumento
if [ -z "$archivo" ]; then
    echo "Error: No se proporcionó ningún archivo"
    echo "Uso: $0 archivo.tex"
    exit 1
fi

# Verificar que el archivo existe
if [ ! -f "$archivo" ]; then
    echo "Error: El archivo '$archivo' no existe"
    exit 1
fi

# Hacer una copia de seguridad del archivo
cp "$archivo" "${archivo}.bak"
echo "Copia de seguridad creada: ${archivo}.bak"

# Contar ocurrencias antes de los cambios
antes=$(grep -c -E '\\hypertarget\{[^}]*\}\{' "$archivo")

echo "Procesando $archivo..."

# Mostrar algunas líneas del archivo para depuración
echo "Muestra del archivo original:"
grep -n -E '\\hypertarget\{[^}]*\}\{' "$archivo" | head -n 3

# Ejecutar sed para limpiar el archivo
sed -z -E -i 's/\\hypertarget\{[^}]*\}\{\s*%?\s*\\(chapter|section|subsection|subsubsection|paragraph|subparagraph)\{([^}]*)\}\\label\{[^}]*\}\}/\\\1{\2}/g' "$archivo"

# Contar ocurrencias después de los cambios
despues=$(grep -c -E '\\hypertarget\{[^}]*\}\{' "$archivo")

# Calcular cuántos reemplazos se hicieron
reemplazos=$((antes - despues))

# Mostrar resultados
echo -e "\nInforme de limpieza:"
echo "Archivo procesado: $archivo"
echo "Reemplazos realizados: $reemplazos"

if [ $reemplazos -eq 0 ] && [ $antes -gt 0 ]; then
    echo "ADVERTENCIA: No se realizaron cambios aunque se encontraron patrones. Posibles razones:"
    echo "1. Las expresiones regulares no están funcionando correctamente"
    echo "2. El formato de los comandos en el archivo es diferente al esperado"
elif [ $reemplazos -eq 0 ] && [ $antes -eq 0 ]; then
    echo "No se encontraron patrones para reemplazar en el archivo."
else
    echo "¡Éxito! Se realizaron $reemplazos reemplazos."
fi

# Verificar si quedaron patrones sin reemplazar
if [ $despues -gt 0 ]; then
    echo -e "\n¡ATENCIÓN! Aún quedan $despues instancias de hypertarget en el archivo."
    echo "Ejemplos de patrones restantes:"
    grep -n -E '\\hypertarget\{[^}]*\}\{' "$archivo" | head -n 3
fi

echo "Limpieza de hypertarget completada."