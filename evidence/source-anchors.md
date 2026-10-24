# 源码证据锚点

以下为原发行件中的局部原文，未执行。S 编号为调查合成索引，不是 REA ID。范围为 0-based UTF-8 bytes、end exclusive；这些片段不能单独证明所有调用路径或启用状态。

<a id="s01"></a>

## S01 · 启动工作目录

模块 `module-001.js`；SHA-256 `0539a26e3e6b7a6c4b69d9783ff7fe0be363c3705319842fbc93333d83392738`；模块字节 `[649, 1244)`；原二进制字节 `[215491137, 215491732)`。

```javascript
import{cwd as e}from"process";function $7r(n){return n.normalize("NFC")}function Sis(n){if(n==="/")return n;return t(n)}function bis(){let n="";if(typeof process<"u"&&typeof process.cwd==="function"&&typeof t==="function")try{let r=e();try{n=$7r(Sis(r))}catch{n=$7r(r)}}catch{}return n}var VTn=bis(),k4t=(()=>{if(typeof process>"u"||typeof process.cwd!=="function")return null;try{return process.cwd()}catch{return null}})();function tRt(){if(k4t===null)return null;let n=process.env.CLAUDE_CODE_SESSION_KIND;return n!==void 0&&String(n).trim()==="bg"?null:k4t}
export{$7r,Sis,bis,VTn,k4t,tRt};

```

<a id="s02"></a>

## S02 · 启动协调与遥测/Hook分支

模块 `module-848.js`；SHA-256 `af82ae1c75b1c8e6abcb6006e15e9f42498ee2b3ae1af0dca0ab79aa7d84d2e0`；模块字节 `[26000, 27520)`；原二进制字节 `[235857265, 235858785)`。

```javascript
ocess.stdout.write(`Resume with: claude --teleport ${Qe}
`)}await Xn(0);return}if(x==="stream-json"||x==="json")c$e(!0);if(Px(),D2()||Ne(process.env.CLAUDE_CODE_ENABLE_TELEMETRY))Zfe(e.storageV5);else tIt(q.host,"telemetry_init",(P)=>{if(P==="shutdown")return;Zfe(e.storageV5)});let lt=(r.continue||r.resume||qe)&&!wdt()?null:_qo(no??io);if(lt&&x!=="json"&&x!=="stream-json")gj(lt);let dt=performance.now(),ut=r.continue||r.resume||qe||st||FI()?void 0:pae(q,{kind:"session-start",source:"startup",storageV5:e.storageV5,credentials:e.credentials}).then((P)=>(Hr("hooks_init_ms",performance.now()-dt,dt),P));ut?.catch(()=>{}),go("before_validateForceLoginOrg");let Oe=pyr(e.orgValidation??await aM(e.credentials));if(!Oe.valid)return $f(Oe.message),eIe(q.host,"shutdown"),await cIe(Oe),await DV({sessionId:V(),message:Oe.message,reason:Oe.reason}),await WWe(),fn();let ze=De?[]:Fe?Fe.then(nke):nke(Ae);if(ze instanceof Promise)ze.catch(()=>{});let pt=uae(),ct={...pt,mainLoopModel:Le,mcp:{...pt.mcp,clients:it,commands:ve,tools:xe},toolPermissionContext:at,proactivityLevel:e.proactivityLevel,...pwt(r.effort),ultracode:dwt(r.effort),autoCompactWindow:w,...Xo()&&{fastMode:E_n(ge??null)},...jC()&&we&&{advisorModel:we},...r.promptSuggestions!==void 0&&{promptSuggestionEnabled:r.promptSuggestions&&MOn()},...We&&{teamContext:We.teamContext,teammateColors:We.teammateColors}},gt=new Apn,K=Ps(ct,(P)=>zPn(P,q,gt,e.storageV5,e.credentials));q.engineStore.adopt(K),RSt(ct.toolPermissionContext.mode),_t(()=>g8t(K.getState().ta
```

<a id="s03"></a>

## S03 · React 元素和 Hooks

模块 `module-489.js`；SHA-256 `79c60bf4f7b6827e488c00d6e41d6de5144cb144548cf3da8cf1aa119388222a`；模块字节 `[4451, 5471)`；原二进制字节 `[225139917, 225140937)`。

```javascript
n(t,e,n){return s.H.useSyncExternalStore(t,e,n)},g$r=function(){return s.H.useTransition()};var j=Ba(()=>{v=Symbol.for("react.transitional.element"),N=Symbol.for("react.portal"),Y=Symbol.for("react.fragment"),I=Symbol.for("react.consumer"),M=Symbol.for("react.context"),L=Symbol.for("react.suspense"),k=Symbol.for("react.memo"),U=Symbol.for("react.lazy"),b=Symbol.for("react.activity"),m=Symbol.iterator;g={isMounted:function(){return!1},enqueueForceUpdate:function(){},enqueueReplaceState:function(){},enqueueSetState:function(){}},q=Object.assign,d={};c.prototype.isReactComponent={};c.prototype.setState=function(t,e){if(typeof t!=="object"&&typeof t!=="function"&&t!=null)throw Error("takes an object of state variables to update or a function which returns an object of state variables.");this.updater.enqueueSetState(this,t,e,"setState")};c.prototype.forceUpdate=function(t){this.updater.enqueueForceUpdate(this,t,"forceUpdate")};h.prototype=c.prototype;x=T.prototype=new h;x.constructor=T;q(x,c.prototype);x.isPur
```

<a id="s04"></a>

## S04 · 终端 Yoga 布局与恢复

模块 `module-579.js`；SHA-256 `077d7c5764866bcd37d4e8f6144197f9cbfc564dc79db83a1b447c622f4c3617`；模块字节 `[335882, 337802)`；原二进制字节 `[232177291, 232179211)`。

```javascript
:R5e.describeLayoutFault(f.retryFault);this.reportLayoutFaultToErrorTracking(m,p),this.logLayoutFaultForDebugging(m,p)}}calculateYogaLayout(n){let u=performance.now();if(this.options.stdout.isTTY||this.options.stdout.columns)n.setWidth(this.terminalColumns),n.calculateLayout(this.terminalColumns);else if(n.setWidthAuto(),n.calculateLayout(),n.getComputedWidth()>Gs)n.setWidth(Gs),n.calculateLayout(Gs);let f=performance.now()-u,m=sy(n);this.lastYogaCounters={ms:f,...m}}relayoutFromScratch(n){try{return n.clearLayoutCacheRecursive(),this.calculateYogaLayout(n),{recovered:!0}}catch(u){try{n.clearLayoutCacheRecursive()}catch{}return{recovered:!1,retryFault:u}}}retryFailedLayout(){let n=this.rootNode.yogaNode;if(!n||!this.relayoutFromScratch(n).recovered)return!1;return this.layoutFailed=!1,this.consecutiveLayoutFailures=0,!0}static describeLayoutFault(n){try{let u=N(n);if(typeof u.message==="string"&&typeof u.name==="string")return u}catch{}return new R("ink layout pass threw a value that cannot be described")}reportLayoutFaultToErrorTracking(n,u){try{if(this.reportLayoutFaultErrorOnce(n),u===void 0){if(!this.reportedLayoutFaultRecovered)this.reportedLayoutFaultRecovered=!0,this.reportLayoutFaultRecovered();return}if(this.reportLayoutFaultErrorOnce(u),!this.reportedLayoutFaultDropped)this.reportedLayoutFaultDropped=!0,this.reportLayoutFaultDropped();if(!this.reportedLayoutFaultPersisting&&this.consecutiveLayoutFailures>=JR)this.reportedLayoutFaultPersisting=!0,this.reportLayoutFaultPersisting()}catch{}}reportLayoutFaultErrorOnce(n){let u=this.reportedLayoutFaultMessages;if(u.has(n.message)||u.size>=ZR)return;u.add(n.message),l(n)}reportLayoutFaultRecovered(){l(new R("ink layout pass threw; recovered by immediate re-layout"))}reportLayoutFaultDropped(){l(new R("ink layout pass threw; immediate re-layout also threw, frame dropped"))}reportLayoutFaultPersisting(){l(new R("ink layout pass still t
```

<a id="s05"></a>

## S05 · Headless 模块导出

模块 `module-1920.js`；SHA-256 `9fd27b57a5b5cb4a0e26483b965ccdb12effb03308860801c833f6e2ea1fc8b3`；模块字节 `[804812, 805086)`；原二进制字节 `[254499266, 254499540)`。

```javascript
eDefaultPickRepoint,oQ as restoreExcludeDynamicSections,nQ as restoreMemoryToggledOff,sQ as restoreProactivityOptIn,sKe as runHeadless,MD as seatMainThreadAgentFromPool,eQ as shouldIgnoreStaleEndSession,pQ as shouldWarnRestrictedStartupModel,$j as updateSettingsGateError};

```

<a id="s06"></a>

## S06 · Prompt snapshot 附件

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[120385, 122105)`；原二进制字节 `[225277268, 225278988)`。

```javascript
.systemTurnsAnsweredBy}}}function svo(e){return e?.systemTurnsAnsweredBy===void 0?e:{...e,systemTurnsAnsweredBy:void 0}}var Hao=new Set(["prompt_snapshot","prompt_render_point","deferred_tools_record"]);function rvt(e){return e.filter((n)=>n.type!=="attachment"||!Hao.has(n.attachment.type))}function O$e(e){return e.type==="attachment"&&e.attachment.type==="prompt_snapshot"}function Uao(e){return e.type==="attachment"&&e.attachment.type==="prompt_render_point"}var nvt=new WeakMap;function LN(e){let n=e.findLast(O$e)?.attachment;if(n===void 0)return;let r=nvt.get(n);if(r)return r;let s=Bao().safeParse(n).data;if(!s)return;let h=s.tools??[],y=Li(s.systemPrompt),b={record:n,systemPrompt:y,systemPromptHash:sWn(y),toolDescriptions:new Map(h.map((w)=>[w.name,w.description])),toolEntries:new Map(h.flatMap((w)=>w.schema!==void 0&&Hzs(w.schema)?[[w.name,w.schema]]:[])),toolServers:new Map(h.flatMap((w)=>w.server===void 0?[]:[[w.name,w.server]])),cliPrefix:s.cliPrefix!==void 0&&oKn(s.cliPrefix)?s.cliPrefix:void 0,reminderFold:s.reminderFold,wireShape:Nnn(s),echoWireToolInputs:s.echoWireToolInputs,contextRendering:s.contextRendering};return nvt.set(n,b),b}function lXe(e,n){return rje(n)&&!oWn(e)?LN(e):void 0}function sge(e,n){return rje(n)?LN(e):void 0}function rWn(e,n){return[...e.toolDescriptions].flatMap(([r,s])=>{if(n?.has(r))return[];let h=e.toolEntries.get(r),y=e.toolServers.get(r);return[{name:r,description:s,...h&&{schema:h},...y!==void 0&&{server:y}}]})}function avt(e,n,r){let s=sge(e,r);if(s===void 0||![...n].some((h)=>s.toolDescriptions.has(h)))return;return{type:"prompt_snapshot",systemPrompt:[...s.systemPrompt],tools:rWn(s,n),...s.cliPrefix!==void 0&&{cliPrefix:s.cliPrefix},...s.reminderFol
```

<a id="s07"></a>

## S07 · 转录记录分类与父消息关系

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[287305, 290025)`；原二进制字节 `[225444188, 225446908)`。

```javascript
envelope,type:"artifact-autoreact-ledger",sessionId:r,accountUuid:s.account,artifacts:Object.fromEntries(y)})}return n}}async function pBe(e){let n=0,r=-1,s,h=-1,y=new Map,b=new Map,w=new Map,H=new Set,q=new Map,K=new Set,Q=(Ge)=>{let Je=Ge.type==="summary"?Ge.leafUuid:Ge.sessionId;return`${Ge.type}:${Je??""}`},Se=new Xue,be=!1,we=[];for await(let Ge of e){we.push(Buffer.byteLength(Ge,"utf8")+1);let Je=Rco(Ge);if(Je){if(Je.type==="file-history-snapshot")b.set(Je.messageId,n);else if(Je.type==="file-history-delta"){let lt=w.get(Je.messageId);if(lt)lt.push(n);else w.set(Je.messageId,[n])}let rt=Eco(Je.type);if(rt==="transcript"){let lt=Je;if(y.set(lt.uuid,{parent:lt.parentUuid,idx:n}),Tco(lt)){if(r=n,s=lt.compactMetadata,!lt.compactMetadata?.preservedSegment&&!lt.compactMetadata?.preservedMessages)h=n}}else if(rt==="accumulate")H.add(n);else if(rt==="last-wins")if(Je.type==="cost-state"&&!Wnn().safeParse(Je).success)H.add(n);else{let lt=Q(Je),pt=q.get(lt);if(pt&&(Je.type==="attribution-snapshot"||Je.type==="artifact-autoreact-ledger"))K.add(pt.idx);if(Je.type==="artifact-autoreact-ledger")Se.add(Je,n);q.set(lt,{idx:n,line:Ge,type:Je.type})}}else if(Ge){H.add(n);let rt=Buffer.from(Ge),lt=rt.subarray(C1(rt,0,rt.length)),pt=c9(lt),kt=pt?cBe(lt):null;if(pt)Se.torn(kt,n);be=kt===null}if(Je)be=!1;n++}let ve=new Map;for(let[Ge,Je]of Se.finish(be)){let rt=q.get(`artifact-autoreact-ledger:${Ge}`);if(rt===void 0)continue;rt.line=_(Je),ve.set(rt.idx,rt.line)}if(r<0)return{kind:"skip"};if(s?.preservedMessages)for(let Ge of s.preservedMessages.uuids){let Je=y.get(Ge);if(!Je)return{kind:"abort",reason:"preserved_uuid_missing"};H.add(Je.idx);let rt=b.get(Ge);if(rt!==void 0)H.add(rt);let lt=w.get(Ge);if(lt)for(let pt of lt)H.add(pt)}else if(s?.preservedSegment){let Ge=s.preservedSegment,Je=Ge.tailUuid,rt=new Set;while(Je&&!rt.has(Je)){rt.add(Je);let lt=y.get(Je);if(lt){H.add(lt.idx);let pt=b.get(Je);if(pt!==void 0)H.add(pt);let kt=w.get(Je);if(kt)for(let dt of kt)H.add(dt);if(Je===Ge.headUuid)break}Je=lt?.parent}if(Je!==Ge.headUuid)return{kind:"abort",reason:"preserved_walk_broken"}}let Ce=new Set;for(let{parent:Ge,idx:Je}of y.values()){if(!Ge||Je<r)continue;let rt=y.get(Ge);if(rt&&rt.idx<r&&!H.has(rt.idx))Ce.add(rt.idx)}for(let Ge of Ce)H.add(Ge);let xe=[];for(let[Ge,{idx:Je}]of y)if(Je<r&&!H.has(Je))xe.push(Ge);let Me={lastBoundaryIdx:r,lastNonPreservedBoundaryIdx:h,keepIdx:H,supersededLastWins:K,lastMeta:q,ledgerSubstitutes:ve,deletedUuids:xe},We=0;for(let Ge=0;Ge<we.length;Ge++)if(!Vxt(Me,Ge))We+=we[Ge];for(let Ge of q.values())if(Yxt(Me,Ge))We-=Buffer.byteLength(Ge.line,"utf8")+1;return{kind:"plan",plan:Me,reclaimableBytes:We}}function Vxt(e,n){return(n>=e.lastBoundaryIdx||e.keepIdx.h
```

<a id="s08"></a>

## S08 · storageV5 反向分页

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[291573, 292993)`；原二进制字节 `[225448456, 225449876)`。

```javascript
t Pco(ZKn(e,n),{force:!0})}catch(s){t(`deleteSessionTitleSidecar: ${d(s)}`,{level:"error"})}}var Oco=262144,Jxt=2097152;async function*xRr(e,n){let r,s,h=Oco,y=!1;for(;;){let b=await e.readRecords(n,y?{order:"backward",limit:2,fromSeq:r}:{order:"backward",maxBytes:h+(s?.byteLength??0),...r!==void 0&&{fromSeq:r}});if(!b.ok){if(b.error.code==="NotFound"&&r===void 0)throw Object.assign(new R("ENOENT: no such file or directory, open (transcript stream)","ENOENT: no such file or directory"),{code:"ENOENT",syscall:"open"});throw t(`[transcript-reverse-read] stream read failed: ${Et(b.error)}`),Error("v5 transcript stream read failed")}let w=b.value.items;if(s!==void 0){let q=w[0];if(q===void 0||q.seq!==r||Buffer.compare(s,q.data)!==0)throw t("[transcript-reverse-read] transcript stream changed between pages; abandoning the scan"),Error("v5 transcript stream changed between pages");w=w.slice(1)}if(w.length===0){if(b.value.nextSeq===void 0)return;y=!0;continue}y=!1;let H;for(let q of w){let{data:K}=q,Q=K.at(-1)===10?K.length-1:K.length,Se=Buffer.from(K.buffer,K.byteOffset,Q).toString("utf8");if(Se)H=q,yield Se}if(b.value.nextSeq===void 0)return;if(H===void 0){h+=Jxt;continue}r=H.seq,s=Buffer.from(H.data),h=Jxt}}var Ico="Windows reported an error (EBADF) when Claude Code read this session's transcript file, although the file had opened normally. This can happen when other software intercepts file reads \u2
```

<a id="s09"></a>

## S09 · JSONL 写入、short write 和 mirror

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[447757, 449777)`；原二进制字节 `[225604640, 225606660)`。

```javascript
,void 0,n)))).flat().map((H)=>({...H,isAlias:!0}));if(b=b9(b.concat(w)),e!==void 0)b=b.slice(0,e)}return await Ppo(b),b}function DPt(e,n){if(Za())return;l0("transcript_metadata",e);let r=ie(),s=_(n)+`
`;try{r.appendFileSync(e,s,{mode:384})}catch{r.mkdirSync(fk(e),{mode:448}),r.appendFileSync(e,s,{mode:384})}Ta().fireMirror(e,[n])}function YBe(e,n,r){if(Za())return;if(J()){pA("transcript_stop_now",e);return}let s=_(n)+`
`,h;try{h=E9(e,yD.O_RDWR|yD.O_APPEND)}catch(y){let b=v(y);if(b==="ENOENT"||b==="ENOTDIR")return;throw y}try{let{size:y}=oHe(h);if(y===0)return;let b=!Bpo(h,y);if(b&&r!==void 0)n=r;let w=Buffer.from(b?`
`+_(n)+`
`:s,"utf8"),H=void 0,q=0;while(q<w.length){let K=QPt(h,w,q,w.length-q,H);if(K<=0)throw Error("appendEntryToExistingFileSync: short write");if(q+=K,H!==void 0)H+=K}}finally{v9(h)}Ta().fireMirror(e,[n])}function Mpo(e){if(J())return"";let n;try{n=E9(e,"r");let r=oHe(n),s=Math.max(0,r.size-Jb),h=Buffer.allocUnsafe(Math.min(Jb,r.size-s)),y=w9(n,h,0,h.length,s);return h.toString("utf8",0,y)}catch{return""}finally{if(n!==void 0)try{v9(n)}catch{}}}var FMt=Wh();function NPt(e){Qd().openAppendRelocationBracket(e)}function LPt(e){let n=Qd().closeAppendRelocationBracket();if(!n)return;for(let{entry:r,storageV5:s,opts:h,resolve:y,reject:b}of n)sx(e,r,s,h).then(y,b)}function sx(e,n,r,s){if(Za())return Promise.resolve();let{relocationParkedAppends:h,relocationParkedPath:y}=Qd();if(h!==null&&e===y)return new Promise((q,K)=>{h.push({entry:n,storageV5:r,opts:s,resolve:q,reject:K})});let b=_(n)+`
`,w=s?.tornTailEntry!==void 0?_(s.tornTailEntry)+`
`:void 0,H=FMt.run(e,async()=>{let q=await k9(e,b,r,s?.onlyIfExists,w);if(q!=="skipped"){let K=(q==="direct-torn"||q==="backend-torn")&&s?.tornTailEntry!==void 0?s.tornTailEntry:n;Ta().fireMirror(e,[K])}});return H.catch((q)=>{t(`appendEntryToFileAsync: append to ${e} failed: ${d(q)}`,{level:"error"})}),H}async function yVn(){await FMt.settle()}function FPt(e){if(!e.includes('"type":"last-prompt"')||!e.includes('"leafUuid":'))return!1;try{
```

<a id="s10"></a>

## S10 · 输入历史 flush

模块 `module-378.js`；SHA-256 `f35ee0ebaf37751f7379cb2dddd3dfb6930cb1e92d9daa1179e816a0f62bc4a4`；模块字节 `[46670, 48190)`；原二进制字节 `[223689078, 223690598)`。

```javascript
tedContents:r}}async flushEntriesToDisk(e){if(this.pendingEntries.length===0)return!0;let n=this.pendingEntries.slice();this.inFlightFlushEntries=new Set(n);while(this.pendingPasteWrites.size>0)await Promise.all(this.pendingPasteWrites);if(e)try{let s=await e.append(je.history(),n.map((y)=>({data:_(y)+`
`})));if(!s.ok){t(`Failed to write prompt history: ${s.error.code}`);let y="telemetryCode"in s.error&&(s.error.telemetryCode==="LockContended"||s.error.telemetryCode==="LockAcquireFailed");return p("history_save",y?"history_save_lock_failed":"history_save_write_failed"),!1}let h=new Set(n);return this.pendingEntries=this.pendingEntries.filter((y)=>!h.has(y)),g("history_save"),!0}catch(s){return t(`Failed to write prompt history: ${s}`),p("history_save","history_save_write_failed"),!1}finally{this.inFlightFlushEntries=null}let r;try{let s=rm(Le(),"history.jsonl");await hn().append(s,"",384),r=await El(s,{...cJe,onCompromised:(w)=>t(`History lock compromised: ${w}`,{level:"error"})});let h=n.map((w)=>_(w)+`
`);await hn().append(s,h.join(""),384);let y=new Set(n);return this.pendingEntries=this.pendingEntries.filter((w)=>!y.has(w)),g("history_save"),!0}catch(s){if(t(`Failed to write prompt history: ${s}`),r)p("history_save","history_save_write_failed");else p("history_save","history_save_lock_failed");return!1}finally{if(this.inFlightFlushEntries=null,r)await r().catch(l)}}async flushWithRetries(e,n){if(this.isWriting||this.pendingEntries.length===0)return;if(e>5)return;this.isWriting=!0;let r=!1;tr
```

<a id="s11"></a>

## S11 · cost-state schema

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[282631, 284151)`；原二进制字节 `[225439514, 225441034)`。

```javascript
keys({inputTokens:!0,outputTokens:!0,cacheReadInputTokens:!0,cacheCreationInputTokens:!0}),Wxt=1000000000000000,wco=Wxt,Wnn=f(()=>{let e=Sn().nonnegative().finite().max(Wxt);return Ct({type:kf("cost-state"),sessionId:ge(),totalCostUSD:e.max(Sco),totalAPIDuration:e,totalAPIDurationWithoutRetries:e,totalToolDuration:e,totalLinesAdded:e,totalLinesRemoved:e,totalDuration:e,startTime:e,modelUsage:uh(ge().regex(/^[^\p{Cc}\p{Cf}]+$/u),Ct({inputTokens:e,outputTokens:e,thinkingTokens:e.optional(),cacheReadInputTokens:e,cacheCreationInputTokens:e,webSearchRequests:e,costUSD:e})).refine((n)=>bco.every((r)=>NHe(Object.values(n),r)<=wco)),hasUnknownModelCost:zo().optional()})});function yWn(e){return e.type==="attachment"&&(e.attachment.type==="cowork_memory_context"||e.attachment.type==="account_memory_recall")&&e.attachment.leg==="laptop"}function Tco(e){return e?.type==="system"&&e.subtype==="compact_boundary"}var vco={user:"transcript",assistant:"transcript",system:"transcript",attachment:"transcript",progress:"boundary-cleared","file-history-snapshot":"boundary-cleared","file-history-delta":"boundary-cleared","last-prompt":"boundary-cleared","continued-in":"boundary-cleared","content-replacement":"accumulate","api-request-shape":"boundary-cleared","api-request-blob":"boundary-cleared","api-request":"boundary-cleared","fork-context-ref":"accumulate","frame-link":"accumulate",summary:"last-wins","custom-title":"last-wins","ended-by-model":"last-wins","ai-title":"last-wins",tag:"last-wins",relocated:"last-
```

<a id="s12"></a>

## S12 · 后台进程配置目录防护

模块 `module-621.js`；SHA-256 `43d832672dac11680625a6a422bafb437d7f998eec203800f833bf8d88e4cac8`；模块字节 `[13985, 15505)`；原二进制字节 `[232497637, 232499157)`。

```javascript
,g=e.env?.PATH||(u?p[u]:void 0);for(let f of Object.keys(o))if(f.toUpperCase()==="PATH")delete o[f];if(g)o[u??"PATH"]=g;if(process.env.CLAUDE_CONFIG_DIR)o.CLAUDE_CONFIG_DIR=process.env.CLAUDE_CONFIG_DIR;else if(o.CLAUDE_CONFIG_DIR!==void 0&&(!_t(o.CLAUDE_CONFIG_DIR)||o.CLAUDE_CONFIG_DIR.split(/[\\/]/).includes("..")||!bie(o.CLAUDE_CONFIG_DIR)))t(`bg spawn ${e.short}: dropped dispatch CLAUDE_CONFIG_DIR \u2014 not an absolute, dot-dot-free spelling of this daemon's config home`,{level:"warn"}),delete o.CLAUDE_CONFIG_DIR;for(let f of QPe)if(!e.env?.[f])delete o[f];if(nte(o),jPt(o),Gms(o,p),!e.env?.CLAUDE_CODE_ENTRYPOINT)QX(o);if(e.isolation==="worktree")o.CLAUDE_BG_ISOLATION="worktree";for(let f of pe)if(!e.env?.[f])delete o[f];for(let f of Object.keys(o))if(_ir.some((A)=>f.startsWith(A))&&!e.env?.[f])delete o[f];if(RKt(p)||Q3e(e)){for(let w of xH)delete o[w];if(Q3e(e)||Ne(p.CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST))AKt(o,e.env);let f=PZ(p);if(f)te(o,[f]),delete o[f];let A=e.env?.CLAUDE_CODE_HOST_CREDS_FILE??(Q3e(e)?p.CLAUDE_CODE_HOST_CREDS_FILE:void 0);if(A)o.CLAUDE_CODE_HOST_CREDS_FILE=A;for(let w of tqe)delete o[w]}else{let f=new Set,A=new Set,w=new Set,E=!1,R=!1;for(let b of dot){let L=b.selection===void 0||Ne(o[b.selection]);if(o[b.endpoint]===p[b.endpoint]&&(!o[b.endpoint]||L)&&b.companions.every((x)=>!gir.includes(x)||Ne(o[x])===Ne(p[x]))){if(o[b.endpoint]){for(let x of b.companions)f.add(x);E||=re(p,b)}continue}for(let x of[b.endpoint,...b.companions])if(A.add(x),o[b.endpoint]&&o[x]!==p[x])w.ad
```

<a id="s13"></a>

## S13 · 配置来源

模块 `module-078.js`；SHA-256 `65859c6671d80357f68a86601d1518449f91908d6a56f74189a57136cf88fa57`；模块字节 `[26507, 27127)`；原二进制字节 `[216377341, 216377961)`。

```javascript
ed??r!==!1)}function zir(e){return Vp(e)||e===Ns}function fK(e){return e.scope==="project"&&e.source.endsWith(`@${Cp}`)}var UKt={policySettings:"managed",userSettings:"user",projectSettings:"project",localSettings:"local",flagSettings:"flag"};function On(e){if(tbe(e))return{name:e.slice(0,e.lastIndexOf("@")),marketplace:Uy};if(e.startsWith("@")&&lxe(e))return{name:e};if(e.includes("@")){let n=e.split("@");return{name:n[0]||"",marketplace:n[1]}}return{name:e}}function lz(e){let n=e.lastIndexOf("@");if(n<0)return{name:e};return{name:e.slice(0,n),marketplace:e.slice(n+1)}}function Tse(e){let n=Zx(e),r=lqe(n);if(r!==
```

<a id="s14"></a>

## S14 · Headless 主引擎绑定

模块 `module-1920.js`；SHA-256 `9fd27b57a5b5cb4a0e26483b965ccdb12effb03308860801c833f6e2ea1fc8b3`；模块字节 `[398703, 399523)`；原二进制字节 `[254093157, 254093977)`。

```javascript
odel:e.fallbackModel,thinkingConfig:e.thinkingConfig,mcpClients:e.mcpClients,mcpResources:{},ideInstallationStatus:null,isNonInteractiveSession:!0,runQuery:yN,customSystemPrompt:e.customSystemPrompt,...e.customSystemPrompt!==void 0&&{omitGitStatus:!0},appendSystemPrompt:e.appendSystemPrompt,planModeInstructions:e.planModeInstructions,systemPromptSnapshot:e.systemPromptSnapshot,appendSubagentSystemPrompt:e.appendSubagentSystemPrompt,toolAliases:e.toolAliases,excludeDynamicSections:e.excludeDynamicSections,agentDefinitions:{activeAgents:e.agents,allAgents:[],allowedAgentTypes:e.allowedAgentTypes},theme:tZt(js("theme","dark").value),maxBudgetUsd:e.maxBudgetUsd,messageClientPlatform:e.messageClientPlatform,forwardSubagentText:e.forwardSubagentText,...n.phase==="query"&&{activeSkill:n.activeSkill},requiresStructur
```

<a id="s15"></a>

## S15 · macOS Keychain 读取、缓存

模块 `module-143.js`；SHA-256 `1e56aa35f197a44c8509e22cc367c50d036b2e35b311c18b680c2ca3f3152f92`；模块字节 `[4367, 6187)`；原二进制字节 `[218484863, 218486683)`。

```javascript
t<sKt)return r.data;let n=e.lastReadFailure;if(n!==null&&Date.now()-n<W8o)return r.data;try{let s=Jj(zRe),a=bI(),o=jFe(`security find-generic-password -a "${a}" -w -s "${s}"`,{timeout:l});if(o){e.keychainHoldsItem=!0;let i=ee(o);return e.cache={data:i,cachedAt:Date.now()},i}}catch(s){}if(r.data!==null)return t("[keychain] read failed; serving stale cache",{level:"warn"}),e.cache={data:r.data,cachedAt:Date.now()},r.data;return e.cache={data:null,cachedAt:Date.now()},null},async readAsync(){let e=Qj(),r=e.cache;if(Date.now()-r.cachedAt<sKt)return r.data;if(e.readInFlight)return e.readInFlight;let n=e.lastReadFailure;if(n!==null&&Date.now()-n<W8o)return null;let s=e.generation,a=F(e).then((o)=>{if(s!==e.generation)return o===ma?null:o;if(e.readInFlight=null,o===ma){if(t("[keychain] readAsync failed; not caching a null",{level:"warn"}),e.lastReadFailure=Date.now(),r.data!==null)e.cache={data:r.data,cachedAt:Date.now()};return r.data}let i=o??r.data;return e.cache={data:i,cachedAt:Date.now()},e.lastReadFailure=null,i});return e.readInFlight=a,a},async readAsyncStrict(e,r){let n=Qj(),s=n.generation,a=await F(n,r);if(a!==ma&&s===n.generation)n.cache={data:a??n.cache.data,cachedAt:Date.now()},n.lastReadFailure=null;return a},invalidateCache(){LL()},mutate(e){return u(b,e)},async update(e){let r=Qj();LL();try{let n=Jj(zRe),s=bI(),a=_(e),o=Buffer.from(a,"utf-8").toString("hex"),i=`add-generic-password -U -a "${s}" -s "${n}" -X "${o}"
`,c;if(i.length<=re)c=await iy("security",["-i"],{input:i,stdio:["pipe","pipe","pipe"],reject:!1,timeout:l});else t(`Keychain payload (${a.length}B JSON) exceeds security -i stdin limit; using argv`,{level:"warn"}),c=await iy("security",["add-generic-password","-U","-a",s,"-s",n,"-X",o],{stdio:["ignore","pipe","pipe"],reject:!1,timeout:l});if(c.exitCode!==0){if(c.exitCo
```

<a id="s16"></a>

## S16 · 遥测/流量策略条件

模块 `module-043.js`；SHA-256 `edbc5aec71746b9a23ac8c1242da099d9019a73fb05aa9c61fea602734c23c00`；模块字节 `[14273, 15293)`；原二进制字节 `[215887387, 215888407)`。

```javascript
e}var z=/<(ide_opened_file|ide_selection)(?:\s[^>]*)?>[\s\S]*?<\/\1>\n?/g;function rmi(t){return t.replace(z,"").trim()}function w3t(){if(process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC)return"essential-traffic";if(process.env.DISABLE_TELEMETRY)return"no-telemetry";if(Ne(process.env.DO_NOT_TRACK))return"no-telemetry";return"default"}function St(){return w3t()==="essential-traffic"}function I1(){return w3t()!=="default"}function dAt(){if(process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC)return"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC";return null}function zYr(){if(process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC)return"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC";if(process.env.DISABLE_TELEMETRY)return"DISABLE_TELEMETRY";if(Ne(process.env.DO_NOT_TRACK))return"DO_NOT_TRACK";return null}function vX(t,e){let r=t.firstPrompt?.startsWith(`<${bX}>`),s=t.firstPrompt?iAt(t.firstPrompt):"",o=s&&!r,a=t.agentName||t.customTitle||t.aiTitle||t.summary||(o?s:void 0)||e||(r?"Autonomous session":void 0)||(t.sessi
```

<a id="s17"></a>

## S17 · 第三方遥测开关与初始化

模块 `module-1654.js`；SHA-256 `6b208a4553199f262a4fc29430026ca3019bde45bd4fac20ea146807939c850c`；模块字节 `[43319, 45039)`；原二进制字节 `[246799648, 246801368)`。

```javascript
{s}`)}}else throw Error(`Unknown exporter type set in OTEL_TRACES_EXPORTER env var: ${n}`);return r.map(Ie("traces",o))}function Bt(){return Ne(process.env.CLAUDE_CODE_ENABLE_TELEMETRY)}function Ut(){let e=k("tengu_cozy_dusk",xe);return typeof e==="number"&&Number.isFinite(e)?Math.min(Math.max(e,xe),xt):xe}function kt(e){let r=new Re({storageV5:e});return _t(()=>r.armShutdownReport()),new U.PeriodicExportingMetricReader({exporter:r,exportIntervalMillis:Ut()})}async function Fn(e,r){if(go("telemetry_init_start"),At(),await bt(),C.propagation.setGlobalPropagator(new me.W3CTraceContextPropagator),Pts())for(let f of["OTEL_METRICS_EXPORTER","OTEL_LOGS_EXPORTER","OTEL_TRACES_EXPORTER"]){let h=process.env[f];if(h?.includes("console"))process.env[f]=h.split(",").map((E)=>E.trim()).filter((E)=>E!=="console").join(",")}C.diag.setLogger(new Omo,i.CLAUDE_CODE_IS_COWORK?C.DiagLogLevel.WARN:C.DiagLogLevel.ERROR),O6s();let o=[],n=Bt(),s=n?be(i.OTEL_METRICS_EXPORTER):[];if(t(`[3P telemetry] isTelemetryEnabled=${n} (CLAUDE_CODE_ENABLE_TELEMETRY=${process.env.CLAUDE_CODE_ENABLE_TELEMETRY})`),n)o.push(...await It(s));if(!r?.disableBigQuery&&je())o.push(kt(e));let u=it();if(WP()){if(!Pit())at();let f=new U.MeterProvider({resource:u,views:[],readers:o});return vLo(f),_t(async()=>{let E=i.CLAUDE_CODE_OTEL_SHUTDOWN_TIMEOUT_MS??2000;try{jCe();let R=OAt(),T=Pit(),L=[f.shutdown()];if(R)L.push(lAe.settledWithin(E/2).then(()=>R.forceFlush()).then(()=>R.shutdown()));if(T)L.push(T.forceFlush().then(()=>T.shutdown()));await Promise.race([Promise.all(L),we(E,"OpenTelemetry shutdown timeout")])}catch{}}),{meter:f.getMeter("com.anthropic.claude_code",de()),metricsExporterKinds:s}}let a=new U.MeterProvider({resource:u,views:[
```

<a id="s18"></a>

## S18 · 遥测初始化协调

模块 `module-640.js`；SHA-256 `af0b65d5de35c22882bfb89b1e469a335a575683a93bc24f16190792a3c9399e`；模块字节 `[11208, 12994)`；原二进制字节 `[232805123, 232806909)`。

```javascript
figuration error in ${p.filePath}: ${p.message}
`),ai(1);return}else throw p}}function Sao(e){return w().promise??=K(e)}function Zfe(e){let r=w();if(QEr()){if(ye()&&WP())E(r,e).catch((f)=>{try{t(`[3P telemetry] Eager telemetry init failed (beta tracing): ${d(f)}`,{level:"error"})}catch{}});t("[3P telemetry] Waiting for remote managed settings fetch before telemetry init"),kN().then(async()=>{t("[3P telemetry] Remote managed settings fetch settled, initializing telemetry"),Px();let{captureAdmin3PSteeringSnapshot:f}=await import("/$bunfs/root/chunk-6pncy4bp.js");f();let[c,n]=await Promise.all([GZ(),kK()]);if(c||n.changed)KZ(),Yb();await E(r,e)}).catch((f)=>{if(xit()&&!r.telemetryInitialized)HXr(EXt()||v0n()?"init_failed":"not_configured");try{t(`[3P telemetry] Telemetry init failed (remote settings path): ${d(f)}`,{level:"error"})}catch{}})}else E(r,e).catch((f)=>{try{t(`[3P telemetry] Telemetry init failed: ${d(f)}`,{level:"error"})}catch{}})}async function E(e,r,f){if(e.telemetryInitialized)return e.telemetryInit;return e.telemetryInitialized=!0,e.telemetryInit=(async()=>{let c="not_configured";try{if(gr("tengu_typed_treasure",{safe:!0}))mzo();await D(r,f)}catch(n){if(e.telemetryInitialized=!1,e.telemetryInit=void 0,EXt())c="init_failed";throw n}finally{HXr(c)}})(),e.telemetryInit}function wXt(){return E(w(),void 0)}function C(e){return(e||"").trim().split(",").filter(Boolean).map((r)=>r.trim()).some((r)=>r!=="none")}function EXt(){return Ne(process.env.CLAUDE_CODE_ENABLE_TELEMETRY)&&C(i.OTEL_LOGS_EXPORTER)}function v0n(){try{let e=fe("policySettings")?.env;if(!e)return!1;return(Ne(process.env.CLAUDE_CODE_ENABLE_TELEMETRY)||Ne(e.CLAUDE_CODE_ENABLE_TELEMETRY))&&(C(i.OTEL_LOGS_EXPORTER)||C(e.OTEL_LOGS_EXPORTER))}catch{return!1}}
export{Sao,Zfe,wXt,EXt,v0n};

```

<a id="s19"></a>

## S19 · 查询入口

模块 `module-745.js`；SHA-256 `1df554fe95d536fc6eee26a8d952da67f349b0f3a27b8147723574f4c048dc07`；模块字节 `[139643, 140863)`；原二进制字节 `[234389739, 234390959)`。

```javascript
r=[typeof e==="string"?e:Array.isArray(e)?e.join(`

`):void 0,o].filter((y)=>!!y);return r.length>0?r.join(`

`):void 0}async function*yN(e){let o=[],n=performance.now();if(Jo(e.querySource)==="main"&&!e.toolUseContext.agentId)tx("engine_pickup");let r=[],y;using s=Pa(e.toolUseContext,e.messages);try{await PJe(e.toolUseContext.options.tools),y=yield*OFn()?kf(e,o,r,s):s.through(ku(e,o,r,s))}finally{let C=e.toolUseContext.agentId;if(C)m6n(e.toolUseContext.session.precompute,C,"subagent_exit",e.querySource,e.toolUseContext.storageV5)}yield*Ll(e.toolUseContext,e.toolUseContext.getAppState,e.querySource,y,Gs);let h=eor(y.reason)?"cancelled":"completed";for(let C of cd(e.toolUseContext.messageQueue,o,!e.toolUseContext.agentId))yield{type:"command_lifecycle",uuid:C,state:h};for(let C of r)yield{type:"command_lifecycle",uuid:C,state:"completed"};if(cNe(y.reason))m("turn",zsi(y));else g("turn");return jd({terminal:y,querySource:e.querySource,agentContext:e.toolUseContext.agentContext,hasActiveGoal:e.toolUseContext.options.activeGoal!==void 0,startedAt:n}),y}async function*kf(e,o,n,r){if(Jo(e.querySource)==="main"){let C=e.toolUseContext.options.agentDefinitions?.activeAgents??[],v=SC(),T=bTs({mainAgentDefiniti
```

<a id="s20"></a>

## S20 · 查询默认依赖

模块 `module-745.js`；SHA-256 `1df554fe95d536fc6eee26a8d952da67f349b0f3a27b8147723574f4c048dc07`；模块字节 `[126106, 126526)`；原二进制字节 `[234376202, 234376622)`。

```javascript
ObservableInput threw")),Pd(n,o)}}function Pd(e,o){return e===Mn?XVt(o)??null:null}import{randomUUID as Xm}from"crypto";function Dd(){return{callModel:YNt,autocompact:SMr,uuid:Xm,now:()=>new Date().toISOString()}}var Lr={maxOutputTokensRecoveryCount:0,hasAttemptedReactiveCompact:!1,reactiveCompactDeeperPass:"none"},zs={...Lr,thinkingOnlyNudged:!1,malformedToolUseRetryCount:0,stopHookBlockingCount:0};function qr(){ret
```

<a id="s21"></a>

## S21 · 流式工具调度器

模块 `module-745.js`；SHA-256 `1df554fe95d536fc6eee26a8d952da67f349b0f3a27b8147723574f4c048dc07`；模块字节 `[53552, 55472)`；原二进制字节 `[234303648, 234305568)`。

```javascript
type==="user"&&Array.isArray(e.message.content)&&e.message.content.some((n)=>n.type==="tool_result"&&n.tool_use_id===o)}class Ls{toolDefinitions;canUseTool;now;tools=[];toolUseContext;discarded=!1;responseOpen=!0;progressAvailableResolve;drainableResolve;drainGeneration=0;appliedLayers=!1;constructor(e,o,n,r){this.toolDefinitions=e;this.canUseTool=o;this.now=r;this.toolUseContext=n}discard(){this.discarded=!0,this.wakeWaiters()}discardAndAbortInFlight(e){this.discard();let o=0,n=0,r=0,y=[];for(let s of this.tools){if(s.status==="completed"||s.status==="yielded"){if(n++,s.status==="completed"&&s.callStarted===!0)y.push(s.id);continue}if(s.status==="queued"){r++;continue}if(s.status==="executing"){if(s.callStarted===!0)y.push(s.id);if(s.abortController&&!s.abortController.signal.aborted)s.abortController.abort(e),o++}}return{aborted:o,completedBeforeEvent:n,queuedNeverStarted:r,toolUseIds:this.tools.map((s)=>s.id),startedToolUseIds:y}}takeFinishedResults(){if(this.discarded)return[];let e=[];for(let o of this.tools)if(o.status==="completed")o.status="yielded",e.push(...o.results);return e}addTool(e,o){let n=Mb(this.toolDefinitions,e.name,this.toolUseContext.options.toolAliases);if(!n&&bNt(e.name,this.toolUseContext)){this.tools.push({id:e.id,block:e,assistantMessage:o,status:"queued",isConcurrencySafe:!1,pendingProgress:[],pendingBridgeEvents:[],results:[]}),this.processQueue();return}if(!n){let s=IAo(e.name,this.toolDefinitions,this.toolUseContext.options.toolCatalog.getAllBaseTools(),this.toolUseContext.agentId,$b(this.toolUseContext),ae(this.toolUseContext),Uzn(this.toolUseContext),e.input,RQe(this.toolUseContext),kcn(this.toolUseContext));PAo(e.name,e.id,this.toolUseContext,o.requestId),this.tools.push({id:e.id,block:e,assistantMessage:o,status:"completed",isConcurrencySafe:!0,pendingProgress:[],pendingBridgeEvents:[],results:[Oe({content:[{type:"tool_result",content:`<tool_use_error>E
```

<a id="s22"></a>

## S22 · Provider factory

模块 `module-231.js`；SHA-256 `0b5caade893c20b57aba8156df78bc691cd7ef270aa3491a26b1defa2ea5ef77`；模块字节 `[262379, 264299)`；原二进制字节 `[220628362, 220630282)`。

```javascript
ole.error("[Anthropic SDK DEBUG]",e,...n)}}function KYn(e,n=[]){return e.map((s)=>("name"in s)?s.name:`mcp__${s.type}`)}async function bF(e){let{apiKey:n,maxRetries:r,model:s,fetchOverride:h,source:b,querySource:y=b,requestClass:w,agentContext:E,promptId:P,ccsSender:H,permissionContext:O,toolNames:M=[],classifierJudgesServedCall:A,credentials:L,storageV5:K,signal:G,clock:Q=Jl,noResponseRetryLedger:z}=e,ee=process.env.CLAUDE_CODE_CONTAINER_ID,X=process.env.CLAUDE_CODE_REMOTE_SESSION_ID,j=process.env.CLAUDE_AGENT_SDK_CLIENT_APP,re=_X()?i.CLAUDE_CODE_SESSION_ORIGIN:void 0,te=Up(E)?void 0:E,ie=IYn(),se=ie?Lni(b,E,w):void 0,ae=ie?Nni(b,E):void 0,ne={userTurn:b!=="side_query"&&Hni(y)&&jG()===void 0&&k_()===void 0&&(E.agentType==="main"||E.isBackgroundAgent===!1)},Be=vjt(),bt=await Tp({querySource:y,permissionContext:O,toolNames:M,classifierJudgesServedCall:A}),je={...ml(),...Be,...o1(),...ee&&{"x-claude-remote-container-id":ee},...X&&{"x-claude-remote-session-id":X},...re&&{[aKr]:re},...j&&{"x-client-app":j},...te?.agentId&&{"x-claude-code-agent-id":z3r(te.agentId)},...te?.parentAgentId&&{"x-claude-code-parent-agent-id":z3r(te.parentAgentId)},...se&&{[Bzt]:se},...ae&&{[sKr]:z3r(ae)},...ie&&P!==void 0&&Vt(P)!==null&&{[iKr]:P}};if(t(`[API:request] Creating client, ANTHROPIC_CUSTOM_HEADERS present: ${!!process.env.ANTHROPIC_CUSTOM_HEADERS}, has Authorization header: ${!!Be.Authorization}`,{level:"verbose"}),i.CLAUDE_CODE_ADDITIONAL_PROTECTION)je["x-anthropic-additional-protection"]="true";if(Te()==="gateway"&&!Wr()&&!Dit()){if(fd())throw z_n("Cloud gateway");throw new Ejt("Not signed in to the Cloud gateway \u2014 run /login.","signin_required")}if(wI()&&lKt())Nh(),uI();let Pt=await Pue({credentials:L,storageV5:K}),jt=Ln(),un=Ltt({anthropicAuthEnabled:nl(),oauthScopes:jt?.scopes}),we=null;if(!un&&!Wr())we=await Sy(je,ye());await Fqe();let dn=Oy(h,b,Od(s),K,Q,z,H),$e=Od(s);if(unt($e),Ci().once("pr
```

<a id="s23"></a>

## S23 · 摘要压缩

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[2544289, 2545809)`；原二进制字节 `[227701172, 227702692)`。

```javascript
=="user"&&n.isVirtual!==!0&&Yh(n)))}function X8e(e){return e.type==="user"&&!e.isMeta&&e.isVirtual!==!0&&!I0(e)&&!Yh(e)}async function yMr(e,n,r,s,h){let{customInstructions:y}=h??{},{isAutoCompact:b=!1,recompactionInfo:w,stripNonEssential:H=!1,spinnerHintText:q,onNotification:K,onResponseLength:Q}=h??{},Se=b?"compact_auto":"compact_manual",be=jK(),we,ve,Ce,xe=performance.now(),Me=c5n("claude_code.compaction",{spanType:"compaction",attrs:{trigger:b?"auto":"manual",message_count:e.length}});try{if(e.length===0)throw m(Se,"compact_not_enough_messages"),Error(Hke);ve=Of(e);let We=n.getAppState();Tsn(ae(n),"summary"),n.onCompactEvent?.({type:"compact_progress",event:{type:"hooks_start",hookType:"pre_compact"}}),n.onCompactEvent?.({type:"sdk_status",status:"compacting"});let Ge=await FMe(n.session,{trigger:b?"auto":"manual",customInstructions:y??null},n,n.abortController.signal);hmn(Ge,K,{suppressNotification:b}),y=mgt(y,Ge.newCustomInstructions);let Je=Ge.userDisplayMessage;n.onCompactEvent?.({type:"stream_mode",mode:"requesting"}),Q?.({type:"response_length",op:"reset"}),n.onCompactEvent?.({type:"compact_progress",event:{type:"compact_start",hintText:q}});let rt=!H&&k("tengu_compact_cache_prefix",!0),lt=ree(),pt=lee(n),kt=nee(y,lt,pt!==void 0),dt=Oe({content:kt}),bt=e,gt=r,At,Gt,zt=0;for(;;){let En=await wmn({messages:bt,summaryRequest:dt,appState:We,context:n,preCompactTokenCount:ve,cacheSafeParams:gt,stripNonEssential:H,onResponseLength:Q,compactionRequestKind:b?"auto":"manual"});if(At=En.response
```

<a id="s24"></a>

## S24 · 自动压缩调度

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[2575361, 2576881)`；原二进制字节 `[227732244, 227733764)`。

```javascript
f(e,r.bytesPerToken)-s+Pje(e),r,n.options.autoCompactWindow).level==="blocked"&&Xr(y)&&Amr(y)&&!$A(li())?y:void 0}async function*SMr(e,n,r,s,h,y,b,w,H=!1){let{model:q}=r,K=n.options.autoCompactWindow;if(w!==void 0&&h!==void 0&&Ooe(h)&&n.session.precompute.get(f$e(n.agentId))?.armTrigger==="idle"){let gt=yield*Mmr(e,n,r,s,h,y,w);if(gt!==void 0)return gt}let Q=s.model!==void 0,Se=(y?.consecutiveFailures??0)>0,be=Q||Se||!hzs()?void 0:Pmr(e,n,r,b),we;if(be!==void 0){let gt=yield*SMr(e,{...n,compactionApiAttemptsLeft:{count:1}},r,{...s,model:be},h,y,b,w,H);if(gt.kind==="compacted")g("compact_larger_model");else if(gt.kind==="failed")p("compact_larger_model",gt.compactFailure?.reason??"failed"),we=gt.consecutiveFailures;if(gt.kind==="compacted"||gt.kind==="hook_blocked"||n.abortController.signal.aborted)return gt}let ve=Ne(process.env.DISABLE_COMPACT),Ce=uRo(h),xe=H&&!lF(),Me=xe?void 0:Imr(n,e,Ce&&!N2n(h,r,K));if(ve)return{kind:"not_needed"};if(Me===void 0&&y?.consecutiveFailures!==void 0&&y.consecutiveFailures>=Umn)return{kind:"failure_breaker_open"};let We=Me!==void 0||xe&&Ce||await xmr(e,r,K,h,b,n.queryTracking,Q);if(Ce&&Vv(h,n.agentId))CXt(n.session,r,K);if(!We)return{kind:"not_needed",consecutiveFailures:we};let Ge=Rmr(e,r,K,b);if(Ge)t(`autocompact: fixed prefix ~${Ge.prefixTokens} > threshold ${Ge.thresholdTokens} \u2014 compaction cannot help`,{level:"warn"}),p("compact_auto","compact_auto_prefix_overflow"),a("tengu_auto_compact_prefix_overflow",{...Ge,wouldHaveBlocked:!0});let Je=vPr(y),{conse
```

<a id="s25"></a>

## S25 · 权限中 Hook allow/deny 处理

模块 `module-499.js`；SHA-256 `642b9ffa0f9b78662cb558971957027f9dbf75d2cb7d9b8425252e44ed09d769`；模块字节 `[4052635, 4055755)`；原二进制字节 `[229209518, 229212638)`。

```javascript
),input:w.input};return w}function KPe(e,n){return(e?.behavior==="allow"||e?.behavior==="ask"?e.updatedInput:void 0)??n}async function T8r(e,n,r,s,h,y,b){if(oG(n))return{decision:{behavior:"allow",updatedInput:r},input:r};let w=mye();if(w!==null)return{decision:w,input:r};let H=s.requireCanUseTool;if(e?.behavior==="deny")return t(`Hook denied tool use for ${n.name}`),qPe(e,{tool:n,input:r,toolUseContext:s,canUseTool:h,assistantMessage:y,toolUseID:b});if(e?.behavior!=="allow"&&e?.behavior!=="ask")return{decision:await h(n,r,s,y,b),input:r};let q=e.behavior,K=KPe(e,r),Q=e.behavior==="ask"?fxr(e,K):e,Se=Q.behavior==="ask"&&Q.hostDisplay!==void 0?Q:void 0,be=M8(K);if(be!==null)return{decision:be,input:K};let we=await BT(n,K,{...s,toolUseId:b},{hookUpdatedInput:e.updatedInput,planModeWriteFloor:q==="allow",hookAsked:q==="ask",...Se!==void 0&&{crashIsObjection:!0}})??await XHs(n,K,s,y,b);if(we?.behavior==="deny")return t(`Hook returned '${q}' for ${n.name}, but deny rule overrides (deny's reason type: ${we.decisionReason?.type??"none"})`),qPe(uye(we),{tool:n,input:K,toolUseContext:s,canUseTool:h,assistantMessage:y,toolUseID:b});if(we?.behavior==="ask"&&Se!==void 0)return m("permission_host_worded_ask","pipeline_also_asks"),{decision:eMe(n.name,"the plain permission prompt raised for this call",{hostWorded:!0}),input:K};if(we?.behavior==="ask"){let ve=q==="ask";return t(`Hook returned '${q}' for ${n.name}, but an ask rule, a safety check, a ToolHost's person-only ask or plan mode requires the full permission pipeline${ve?" (hookAskFloor \u2014 a classifier allow re-surfaces as this ask)":""}`),{decision:await h(n,K,ve?{...s,hookAskFloor:!0}:s,y,b),input:K}}if(q==="allow"){if(H)return t(`Hook approved tool use for ${n.name}, but canUseTool is required`),{decision:await h(n,K,s,y,b),input:K};let ve=ae(s),Ce=tu(n,ve),xe=Ls(Ce)&&Nmn(n),Me=!xe&&Ce==="auto"&&k("tengu_virtual_knuth",!1),We=!xe&&!Me&&mB(n,ve),Ge=!xe&&!Me&&SN(n,ve),Je=!xe&&!Me&&!We&&!Ge&&ZD(n);if(!n.requiresUserInteraction?.()&&(xe||Me||We||Ge||Je)){let rt=e.decisionReason?.type==="hook"?e.decisionReason:void 0,lt=!Je||Ls(Ce);if(lt)a("tengu_auto_mode_hook_allow_funneled",{toolName:Nn(n.name),isMcp:n.isMcp??!1,remoteSessionMcp:We,coworkWeb:Ge,hookSource:ce(_qe(rt?.hookSource)),agentMsgId:_e(y.message.id),toolUseId:_e(b)});return t(lt?`Hook approved tool use for ${n.name}, but auto mode requires classifier adjudication`:`Hook approved tool use for ${n.name}, but a hook cannot approve a call to CCR's cloud browser; the normal permission check decides`),{decision:await h(n,K,{...s,hookAllowVouched:!0},y,b),input:K}}return t(n.requiresUserInteraction?.()?`Hook satisfied user interaction for ${n.name} via updatedInput`:`Hook approved tool use for ${n.name}, bypassing permission prompt`),ZCo("preToolUseHook",n,K,s,y,b),qPe(e,{tool:n,input:K,toolUseContext:s,canUseTool:h,assistantMessage:y,toolUseID:b})}return qPe(Q,{tool:n,input:K,toolUseContext:s,canUseTool:h,assistantMessage:y,toolUseID:b})}async function qPe(e,n){let r=await mIr({tool:n.tool,input:n.input,context:n.toolUseContext,toolUseID:n.toolUseID,evaluate:()=>Pr
```

<a id="s26"></a>

## S26 · 插件刷新

模块 `module-1201.js`；SHA-256 `971881f504ef88788c3569b6536b2db3e10a240683d500b7df81b23a5def6c4e`；模块字节 `[1765, 4485)`；原二进制字节 `[239947388, 239950108)`。

```javascript
var v=(n)=>Object.entries(n??{}).filter(([,e])=>e.pluginSource!==void 0).map(([e])=>e);async function Vbr(n,e){return 0}async function P$(n,e,c,y={}){let u=y.applyStagedInstalls??!0,f=lN(),{changesLanded:h,holdsSet:k}=f;using p={[Symbol.dispose]:()=>{f.endHoldSetBefore(k)}};let i=Ie().organizationAsk,w=u&&My()!=="unanswered"?i.heldReresolve:null;if(w)i.heldReresolve=null,await w().catch(l);if(t("refreshActivePlugins: clearing all plugin caches"),u)ali(),jFs();if(Dd(e,c),u)C0s();let o=await iE(e,c);cxo();let L=Ie().pluginLoadCacheOnly;await _To(e),ze.refreshConfig();let[S,j,b]=await Promise.all([Pge(e),Hje(e),UA(ke(),e)]),{enabled:g,disabled:R,errors:B,warnings:N}=o,_=[],E=[],[T,x]=await Promise.all([Promise.all(g.map(async(r)=>{let s=await Tft(r,_,e,{warnings:E});return s?Object.keys(s).length:0})),Promise.all(g.map(async(r)=>{if(r.lspServers)return Object.keys(r.lspServers).length;let s=await RXe(r,_,e);if(s)r.lspServers=s;return s?Object.keys(s).length:0}))]),C=T.reduce((r,s)=>r+s,0),I=x.reduce((r,s)=>r+s,0);await Vbr(g,_);let O=[...N,...E,...y2n(g)],A=[...B,..._];n.applyRefresh({enabled:g,disabled:R,commands:S,errors:A,warnings:O,agentDefinitions:b}),_2n(e,c);let P=!1;try{await Q9(e,c)}catch(r){P=!0,l(r),t(`refreshActivePlugins: loadPluginHooks failed: ${d(r)}`)}if(!P)await uin(g,e).catch(l),f.reloaded(h);let D=g.reduce((r,s)=>{if(!s.hooksConfig)return r;return r+Object.values(s.hooksConfig).reduce((G,z)=>G+(z?.reduce((H,J)=>H+J.hooks.length,0)??0),0)},0),M=br();M.isAnnouncingFreshLoad=L!==void 0&&Ie().pluginLoadCacheOnly===L;try{g2.emit()}finally{M.isAnnouncingFreshLoad=!1}return t(`refreshActivePlugins: ${g.length} enabled, ${S.length} commands, ${j.length} skills, ${b.allAgents.length} agents, ${D} hooks, ${C} MCP, ${I} LSP`),{enabled_count:F(g,(r)=>r.isBuiltin!==!0),disabled_count:F(R,(r)=>r.isBuiltin!==!0),command_count:S.length,skill_count:j.length,agent_count:b.allAgents.length,hook_count:D,mcp_count:C,lsp_count:I,error_count:A.length+(P?1:0),errors:A,warnings:O,agentDefinitions:b,pluginCommands:S}}async function a7(n){let e=new Set(n.mcpClients.filter((o)=>o.config.pluginSource!==void 0).map((o)=>o.name)),c,y=()=>c??=Vke(n.storageV5),u=await Pxo(n.dynamicMcpConfig??{},n.storageV5,y,ame());for(let o of v(n.dynamicMcpConfig))u.add(o);let f=[...u].filter((o)=>!e.has(o)).sort(),h=[...e].filter((o)=>!u.has(o)).sort(),k=f.length>0||h.length>0,p=oh()&&bce(n.model)&&!Sce(n.model),i=cy()>0,m=null;if(uGe()&&!p&&i&&!mr("lspServers")){let o=kko()?{hasServers:!1,loaderFailed:!1,loaderFailedApplyHealable:!1,derivationFailed:!1}:await K(y,n.storageV5,n.credentials);if(!vje()){if(o.hasServers)m="adds";else if(o.loaderFailedApplyHealable)m="may-add"}else if(!o.hasServers&&!o.de
```

<a id="s27"></a>

## S27 · MCP 服务端调用内置工具

模块 `module-2484.js`；SHA-256 `1f8362148a16fa4e7e19e9f796bd996867ac96200688473e8c94055e975eb614`；模块字节 `[12185, 13405)`；原二进制字节 `[264153675, 264154895)`。

```javascript
{type:"text",text:C.rejection}],...C.meta!==void 0&&{_meta:C.meta}};using q=Z(s?.progressToken,x);let j=await v.run(()=>T.call(n.data,{...C.toolUseContext,permissionPhase:C.toolUseContext.permissionPhase??{}},rE,Ld({content:[]}),void 0,I==="raw"?{gitDiffRead:!0}:E?{smallResultAsked:!0}:void 0)),M,V=!1;if(X){let{encodeUnlistedToolResult:o}=await import("/$bunfs/root/chunk-bt8zv68s.js");M=v.run(()=>o(T,j))}else if(I==="rendered"){let{renderToolResultForMCP:o,withinAnswerLimit:L}=await import("/$bunfs/root/chunk-s1pnaaqz.js"),{answer:G,tooLarge:W}=L(T,await v.run(()=>o(T,j,re)));M=E?await(await import("/$bunfs/root/chunk-9g2rga8g.js")).withEditResult(G,j):G,V=W}if(M===void 0){let o=j.data,L=typeof o==="object"&&o!==null&&"backgroundTaskId"in o&&typeof o.backgroundTaskId==="string"?{...o,backgroundOutputPath:Ou(o.backgroundTaskId)}:o;M={content:[{type:"text",text:_(L)}]}}if(y.length>0){let o=Xit(y),L=M.content.at(-1);if(L?.type==="text")L.text+=`
${o}`;else M.content.push({type:"text",text:o})}if(!ue)if(V)p(kNt(T.name),"result_too_large");else g(kNt(T.name));return z(M)}catch(r){let n=(r instanceof Error?zCo(r):[String(r)]).filter(Boolean).join(`
`).trim()||"Error";if(p7e(r))t(`MCP server tool call '${e}'
```

<a id="s28"></a>

## S28 · 交互主引擎绑定

模块 `module-1892.js`；SHA-256 `253fa07d8cd8ac4de1e65510125b6d74c6bbf19c44165f53e04614ab16778571`；模块字节 `[1496022, 1496842)`；原二进制字节 `[252784858, 252785678)`。

```javascript
jo.thinkingDisplayOverride,et),mcpClients:be.computeMcpClients(),mcpResources:jo.mcp.resources,ideInstallationStatus:dt,isNonInteractiveSession:!1,runQuery:yN,resolveCommandDialog:yt,renderDebugControls:Ws().get(process.stdout)?.renderDebug,requiresStructuredOutput:Jo.some((ln)=>Rt(ln,Ya)),dynamicMcpConfig:be.dynamicMcpConfig,theme:xt,agentDefinitions:Dn?{...jo.agentDefinitions,allowedAgentTypes:Dn}:jo.agentDefinitions,customSystemPrompt:bt,appendSystemPrompt:At,systemPromptSnapshot:Dt,refreshTools:be.computeTools,refreshMcpClients:be.computeMcpClients,autoCompactWindow:jo.autoCompactWindow,fastMode:jo.fastMode,cacheBreakerPhrase:jo.cacheBreakerPhrase,activeGoal:jo.activeGoal,ultraplanSessionUrl:jo.ultraplanSessionUrl},getAppState:()=>Z.getState(),setAppState:(ln)=>Wo(()=>Ht(ln)),...Ect(()=>Z.getState(),Ot),q
```
