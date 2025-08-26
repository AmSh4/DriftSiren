'use client';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';

export default function Chart({data}:{data:{time:string, psi:number, ks:number, chi2:number}[]}){
  return (
    <div className="h-64">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="psi" dot={false} />
          <Line type="monotone" dataKey="ks" dot={false} />
          <Line type="monotone" dataKey="chi2" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
