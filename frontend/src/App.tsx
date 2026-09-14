import { useState } from 'react'
import './App.css'
import { DoctorPortal } from './components/DoctorPortal'
import { PatientPortal } from './components/PatientPortal'
import { RoleSwitcher, type AppRole } from './components/RoleSwitcher'

function App() {
  const [role, setRole] = useState<AppRole>('patient')

  return (
    <div style={{ minHeight: '100vh', background: '#f8fafc', color: '#0f172a' }}>
      <header
        style={{
          position: 'sticky',
          top: 0,
          zIndex: 10,
          width: '100%',
          background: 'rgba(255,255,255,0.88)',
          backdropFilter: 'blur(10px)',
          borderBottom: '1px solid #e2e8f0',
        }}
      >
        <div
          style={{
            maxWidth: 1280,
            margin: '0 auto',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '18px 24px',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <div
              style={{
                width: 32,
                height: 32,
                borderRadius: 12,
                background: role === 'patient' ? '#0ea5e9' : '#1d4ed8',
                display: 'grid',
                placeItems: 'center',
                color: '#fff',
                fontWeight: 700,
              }}
            >
              M
            </div>
            <div>
              <div style={{ fontWeight: 700 }}>MediAI</div>
              <div style={{ fontSize: 12, color: '#64748b' }}>
                {role === 'patient' ? 'Patient portal' : 'Doctor portal'}
              </div>
            </div>
          </div>

          <RoleSwitcher value={role} onChange={setRole} />

          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <button
              style={{
                background: '#f1f5f9',
                border: '1px solid #e2e8f0',
                borderRadius: 10,
                padding: '10px 12px',
              }}
            >
              {role === 'patient' ? 'Search' : 'Filters'}
            </button>
            <div
              style={{
                width: 36,
                height: 36,
                borderRadius: '50%',
                background: '#dbeafe',
                display: 'grid',
                placeItems: 'center',
                fontWeight: 700,
              }}
            >
              {role === 'patient' ? 'AM' : 'OC'}
            </div>
          </div>
        </div>
      </header>

      <main style={{ maxWidth: 1280, margin: '0 auto', padding: '30px 24px 48px' }}>
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: 24,
          }}
        >
          <div>
            <div
              style={{
                color: role === 'patient' ? '#0ea5e9' : '#2563eb',
                fontSize: 13,
                fontWeight: 700,
                letterSpacing: '0.08em',
                textTransform: 'uppercase',
              }}
            >
              {role === 'patient' ? 'Overview' : 'Clinical overview'}
            </div>
            <h1 style={{ margin: '8px 0 0', fontSize: 32 }}>
              {role === 'patient' ? 'Welcome back, Ava' : 'Welcome back, Dr. Chen'}
            </h1>
          </div>
          <button
            style={{
              background: '#0f172a',
              color: '#fff',
              border: 'none',
              borderRadius: 12,
              padding: '12px 18px',
              fontWeight: 600,
            }}
          >
            {role === 'patient' ? 'Book appointment' : 'New consultation'}
          </button>
        </div>

        {role === 'patient' ? <PatientPortal /> : <DoctorPortal />}
      </main>
    </div>
  )
}

export default App
