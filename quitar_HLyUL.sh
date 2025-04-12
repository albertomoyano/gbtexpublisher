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

# Mostrar algunas líneas del archivo para depuración
echo "Primeras 10 líneas del archivo original:"
head -n 10 "$archivo"

# Usar un script de sed más simple pero efectivo
sed -i '
    s/\\hl{}/  /g
    s/\\ul{}/  /g
    s/\\hl{\\ul{\([^}]*\)}}/\1/g
    s/\\ul{\\hl{\([^}]*\)}}/\1/g
    s/\\hl{\([^}]*\)}/\1/g
    s/\\ul{\([^}]*\)}/\1/g
' "$archivo"

# Mostrar algunas líneas después de la modificación
echo -e "\nPrimeras 10 líneas del archivo después de la modificación:"
head -n 10 "$archivo"

# Verificar si quedaron patrones sin reemplazar
patrones_restantes=$(grep -c -E '\\hl\{|\\ul\{' "$archivo")

echo -e "\nInforme de limpieza:"
if [ "$patrones_restantes" -gt 0 ]; then
    echo "¡ATENCIÓN! Aún quedan $patrones_restantes instancias de los patrones en el archivo."
    echo "Líneas con patrones restantes:"
    grep -n -E '\\hl\{|\\ul\{' "$archivo" | head -n 5
else
    echo "¡Éxito! Todos los patrones fueron reemplazados correctamente."
fi

echo "Limpieza de comandos LaTeX terminada."