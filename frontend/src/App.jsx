import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [incidents, setIncidents] = useState([])

  const fetchData = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/incidents')
      setIncidents(res.data)
    } catch (err) {
      console.error("Error", err)
    }
  }


  const handleClear = async () => {
    if (window.confirm("Are you sure?")) {
      try {
        await axios.delete('http://127.0.0.1:8000/incidents')
        setIncidents([]) 
      } catch (err) {
        alert("Error")
      }
    }
  }

  useEffect(() => {
    fetchData()
    const interval = setInterval(fetchData, 5000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 p-10 font-sans">
      <header className="mb-10 border-b border-slate-800 pb-6 flex justify-between items-end">
        <div>
          <h1 className="text-4xl font-extrabold text-sky-400 tracking-tight leading-none">
              AI Log Analyzer
          </h1>
          <p className="text-slate-400 mt-2 text-sm uppercase tracking-widest font-medium">
            Real-time Security Monitoring | <span className="text-emerald-500">using Llama 3.2 3b</span>
          </p>
        </div>

        <div className="flex items-center gap-6">
          <button 
            onClick={handleClear}
            className="text-[10px] font-bold tracking-widest uppercase px-3 py-1.5 bg-red-500/10 border border-red-500/20 text-red-500 hover:bg-red-500 hover:text-white transition-all rounded"
          >
            Clear Database
          </button>
          
          <div className="flex items-center gap-2">
            <span className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
            </span>
            <span className="text-xs text-slate-500 font-mono">LIVE FEED</span>
          </div>
        </div>
      </header>

      <div className="grid gap-6 max-w-6xl mx-auto">
        {incidents.length === 0 ? (
          <div className="text-center py-20 text-slate-600 border-2 border-dashed border-slate-900 rounded-xl">
            Database is empty
          </div>
        ) : (
          incidents.map(item => (
            <div 
              key={item.id} 
              className={`bg-slate-900 p-6 rounded-xl border-l-4 shadow-xl transition-all duration-300 hover:scale-[1.01] ${
                item.level === 'ERROR' ? 'border-red-500 shadow-red-900/10' : 'border-amber-500 shadow-amber-900/10'
              }`}
            >
              <div className="flex justify-between items-center mb-4">
                <span className={`px-3 py-1 rounded text-xs font-bold tracking-wider ${
                  item.level === 'ERROR' ? 'bg-red-500/10 text-red-400' : 'bg-amber-500/10 text-amber-400'
                }`}>
                  [{item.level}] {item.timestamp}
                </span>
                <span className="text-slate-600 font-mono text-sm">ID: #{item.id}</span>
              </div>

              <div className="bg-black/50 p-4 rounded-lg border border-slate-800 mb-4 shadow-inner">
                <p className="font-mono text-sm text-slate-300 break-all leading-relaxed">
                  <span className="text-slate-600 mr-2">$</span>
                  {item.content}
                </p>
              </div>

              <div className="flex items-start gap-3 bg-emerald-950/20 p-4 rounded-lg border border-emerald-900/30">
                <span className="text-emerald-400 font-bold shrink-0 text-sm mt-0.5">AI Solution:</span>
                <p className="text-emerald-200/90 text-[0.95rem] italic leading-snug">
                  "{item.solution}"
                </p>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default App