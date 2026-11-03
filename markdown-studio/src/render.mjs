const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function inline(text){return esc(text).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replace(/\*([^*]+)\*/g,'<em>$1</em>');}
export function renderMarkdown(source){
 const out=[],lines=source.replace(/\r/g,'').split('\n');let para=[],list=false,code=false,codeLines=[];
 const flush=()=>{if(para.length){out.push(`<p>${inline(para.join(' '))}</p>`);para=[];}};
 const closeList=()=>{if(list){out.push('</ul>');list=false;}};
 for(const line of lines){
  if(line.startsWith('```')){flush();closeList();if(code){out.push(`<pre><code>${esc(codeLines.join('\n'))}</code></pre>`);codeLines=[];}code=!code;continue;}
  if(code){codeLines.push(line);continue;}
  const heading=line.match(/^(#{1,3})\s+(.+)$/);if(heading){flush();closeList();const level=heading[1].length;out.push(`<h${level}>${inline(heading[2])}</h${level}>`);continue;}
  const item=line.match(/^\s*[-*]\s+(.+)$/);if(item){flush();if(!list){out.push('<ul>');list=true;}out.push(`<li>${inline(item[1])}</li>`);continue;}
  if(!line.trim()){flush();closeList();continue;}closeList();para.push(line.trim());
 }
 flush();closeList();if(code)out.push(`<pre><code>${esc(codeLines.join('\n'))}</code></pre>`);
 return out.join('\n');
}
export function makeSearchIndex(documents){return documents.map(({slug,title,body})=>({slug,title,terms:[...new Set((title+' '+body).toLowerCase().match(/[a-z0-9]+/g)??[])]}));}
export function page(title,body){return `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${esc(title)} · Notes</title><link rel="stylesheet" href="style.css"><body><nav><a href="index.html">Markdown Studio</a><input id="search" placeholder="Search notes" aria-label="Search notes"></nav><main><h1>${esc(title)}</h1>${body}</main><script src="search.js" defer></script></body></html>`;}
