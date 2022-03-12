#!/usr/bin/env texlua

module = "ustcthesis"

testfiledir = "./test/testfiles"
testsuppdir = "./test/support"

demofiles = {"main.tex", "bib", "chapters"}
installfiles = {"*.cls", "*.bst", "*.bbx", "*.cbx", "figures"}
sourcefiles = {"*.cls", "*.bst", "*.bbx", "*.cbx", "figures"}
tagfiles = {"*.cls", "ustcthesis-doc.tex", "CHANGELOG.md"}

checkengines = {"xetex"}
stdengine = "xetex"

checkconfigs = {
    "build",
    "test/config-crossref",
    "test/config-nomencl",
    "test/config-bibtex",
    "test/config-biblatex",
}

typesetexe = "xelatex"
unpackexe = "xetex"

checkopts = "-file-line-error -halt-on-error -interaction=nonstopmode"
typesetopts = "-file-line-error -halt-on-error -interaction=nonstopmode"

lvtext = ".tex"

function update_tag(file, content, tagname, tagdate)
  tagname = string.gsub(tagname, "^v", "")
  local url = "https://github.com/ustctug/ustcthesis"

  if string.match(file, "%.cls$") then
    content = string.gsub(content, "\\def\\ustcthesisversion{[^}]*}",
    "\\def\\ustcthesisversion{" .. tagname .. "}" )

    content = string.gsub(content,
      "\\ProvidesExplClass {ustcthesis} {[^}]*} {[^}]*}",
      "\\ProvidesExplClass {ustcthesis} {" .. tagdate .. "} {\\ustcthesisversion}")

  elseif string.match(file, "%-doc%.tex$") then
    content = string.gsub(content,
      "\\date{.*\\qquad %d%d%d%d%-%d%d%-%d%d}",
      "\\date{v" .. tagname .. " \\qquad " .. tagdate .. "}")

  elseif string.match(file, "CHANGELOG.md") then
    local previous = string.match(content, "/compare/v(.*)%.%.%.HEAD")

    if tagname == previous then return content end
    content = string.gsub(content,
      "## %[Unreleased%]",
      "## [Unreleased]\n\n## [v" .. tagname .."] - " .. tagdate)
    content = string.gsub(content,
      previous .. "%.%.%.HEAD",
      tagname .. "...HEAD\n[v" .. tagname .. "]: " .. url ..
      "/compare/v" .. previous .. "..." .. "v" .. tagname)
  end
  return content
end
