export default function Card({ title, children }:{title:string, children: React.ReactNode}){
  return (
    <div className="card">
      <div className="flex items-center justify-between mb-3">
        <h3 className="font-semibold">{title}</h3>
      </div>
      {children}
    </div>
  )
}
