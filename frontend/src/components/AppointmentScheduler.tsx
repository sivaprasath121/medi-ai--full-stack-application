import { useState } from 'react'

type AppointmentForm = {
  patient_id: string
  doctor_id: string
  date: string
  time: string
  reason: string
  status: string
}

const initialForm: AppointmentForm = {
  patient_id: 'patient-001',
  doctor_id: 'doctor-001',
  date: '2026-09-20',
  time: '09:30',
  reason: 'Follow-up consultation',
  status: 'scheduled',
}

export function AppointmentScheduler() {
  const [form, setForm] = useState<AppointmentForm>(initialForm)
  const [message, setMessage] = useState('')

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    const response = await fetch('http://localhost:8000/api/appointments', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })

    if (!response.ok) {
      setMessage('Unable to schedule appointment.')
      return
    }

    const payload = await response.json()
    setMessage(`Appointment booked for ${payload.patient_name} with ${payload.doctor_name} on ${payload.date} at ${payload.time}.`)
    setForm(initialForm)
  }

  return (
    <form onSubmit={handleSubmit} style={{ display: 'grid', gap: 14, background: '#fff', borderRadius: 18, border: '1px solid #e5e7eb', padding: 20 }}>
      <div style={{ fontWeight: 700, fontSize: 20 }}>Schedule appointment</div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 12 }}>
        <label style={{ display: 'grid', gap: 6 }}>
          <span style={{ fontSize: 12, color: '#64748b' }}>Patient</span>
          <select value={form.patient_id} onChange={(e) => setForm({ ...form, patient_id: e.target.value })} style={fieldStyle}>
            <option value="patient-001">Ava Martinez</option>
            <option value="patient-002">Daniel Nguyen</option>
          </select>
        </label>

        <label style={{ display: 'grid', gap: 6 }}>
          <span style={{ fontSize: 12, color: '#64748b' }}>Doctor</span>
          <select value={form.doctor_id} onChange={(e) => setForm({ ...form, doctor_id: e.target.value })} style={fieldStyle}>
            <option value="doctor-001">Dr. Olivia Chen</option>
          </select>
        </label>

        <label style={{ display: 'grid', gap: 6 }}>
          <span style={{ fontSize: 12, color: '#64748b' }}>Date</span>
          <input type="date" value={form.date} onChange={(e) => setForm({ ...form, date: e.target.value })} style={fieldStyle} />
        </label>

        <label style={{ display: 'grid', gap: 6 }}>
          <span style={{ fontSize: 12, color: '#64748b' }}>Time</span>
          <input type="time" value={form.time} onChange={(e) => setForm({ ...form, time: e.target.value })} style={fieldStyle} />
        </label>
      </div>

      <label style={{ display: 'grid', gap: 6 }}>
        <span style={{ fontSize: 12, color: '#64748b' }}>Reason</span>
        <input
          value={form.reason}
          onChange={(e) => setForm({ ...form, reason: e.target.value })}
          style={fieldStyle}
          placeholder="Follow-up consultation"
        />
      </label>

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 12, flexWrap: 'wrap' }}>
        <button type="submit" style={{ background: '#111827', color: '#fff', border: 'none', borderRadius: 12, padding: '12px 18px', fontWeight: 700 }}>
          Save appointment
        </button>
        {message ? <span style={{ color: '#0f766e', fontWeight: 600 }}>{message}</span> : null}
      </div>
    </form>
  )
}

const fieldStyle: React.CSSProperties = {
  border: '1px solid #dbeafe',
  background: '#f8fafc',
  borderRadius: 10,
  padding: '12px 14px',
  fontSize: 14,
  color: '#0f172a',
}
