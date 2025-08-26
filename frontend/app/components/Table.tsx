export default function Table({ columns, rows }:{columns:string[], rows:any[]}){
  return (
    <div className="overflow-auto">
      <table className="min-w-full text-sm">
        <thead><tr>{columns.map(c => <th key={c} className="text-left p-2 border-b">{c}</th>)}</tr></thead>
        <tbody>
          {rows.map((r,i)=>(
            <tr key={i} className="odd:bg-gray-50/50 dark:odd:bg-gray-800/50">
              {columns.map(c => <td key={c} className="p-2 border-b">{String(r[c] ?? "")}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
