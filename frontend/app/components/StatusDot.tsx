export default function StatusDot({ ok }:{ ok:boolean }){
  return <span className={"inline-block w-2.5 h-2.5 rounded-full " + (ok ? "bg-green-500" : "bg-red-500")} />
}
