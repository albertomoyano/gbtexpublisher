function RawInline(el)
  if el.format == "latex" then
    el.text = el.text:gsub("\\hl%{(.*)%}", "%1")
  end
  return el
end