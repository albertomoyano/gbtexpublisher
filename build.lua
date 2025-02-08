if mode=="draft" then 
  Make:htlatex {} 
else 
  Make:htlatex {} 
  Make:biber {} 
  Make:htlatex{} 
  Make:htlatex{}
end
Make:htlatex {} 
Make:xindy {}
Make:xindy {idxfile = "names.idx"} 
Make:xindy {idxfile = "foo.idx"}
Make:xindy {idxfile = "foo2.idx"} 
Make:xindy {idxfile = "foo3.idx"} 
Make:htlatex {}
Make:htlatex {}
