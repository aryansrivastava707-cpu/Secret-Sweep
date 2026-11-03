import test from 'node:test';import assert from 'node:assert/strict';import {renderMarkdown,makeSearchIndex,page} from '../src/render.mjs';
test('renders headings and list items',()=>{const html=renderMarkdown('# Title\n\n- one\n- two');assert.match(html,/<h1>Title<\/h1>/);assert.equal((html.match(/<li>/g)||[]).length,2)});
test('escapes raw HTML inside text and code fences',()=>{const html=renderMarkdown('<script>x</script>\n\n```html\n<img>\n```');assert.doesNotMatch(html,/<script>|<img>/);assert.match(html,/&lt;script&gt;/)});
test('creates unique search terms and escapes page titles',()=>{assert.deepEqual(makeSearchIndex([{slug:'a',title:'Green green',body:'Green leaf'}])[0].terms,['green','leaf']);assert.match(page('<script>',''),/&lt;script&gt;/)});
