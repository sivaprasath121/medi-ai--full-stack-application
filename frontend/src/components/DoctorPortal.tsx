import { useEffect, useState } from 'react'
import { AppointmentScheduler } from './AppointmentScheduler'

type DoctorOverview = {
  id: string
  name: string
  specialty: string
  clinic_status: string
  today_patients: number
  appointments_today: number
  pending_reviews: number
  avg_wait_time: string
  next_round: string
}

type QueueItem = {
  patient_id: string
  patient_name: string
  time: string
  status: string
  visit_type: string
  priority: string
}

const cardStyles = {
  emerald: 'rgba(16,185,129,0.1)',
  blue: 'rgba(59,130,246,0.1)',
  violet: 'rgba(139,92,246,0.1)',
  amber: 'rgba(245,158,11,0.1)',
  rose: 'rgba(244,63,94,0.1)',
}

export function DoctorPortal() {
  const [overview, setOverview] = useState<DoctorOverview | null>(null)
  const [queue, setQueue] = useState<QueueItem[]>([])

  useEffect(() => {
    Promise.all([
      fetch('http://localhost:8000/api/doctors/overview'),
      fetch('http://localhost:8000/api/doctors/patients'),
    ])
      .then(async ([overviewRes, queueRes]) => {
        const overviewData = await overviewRes.json()
        const queueData = await queueRes.json()
        setOverview(overviewData)
        setQueue(queueData)
      })
      .catch(() => {
        setOverview({
          id: 'doctor-001',
          name: 'Dr. Olivia Chen',
          specialty: 'Cardiology',
          clinic_status: 'On schedule',
          today_patients: 18,
          appointments_today: 12,
          pending_reviews: 6,
          avg_wait_time: '14 min',
          next_round: '10:30 AM',
        })
        setQueue([
          {
            patient_id: 'patient-001',
            patient_name: 'Ava Martinez',
            time: '10:30 AM',
            status: 'In consultation',
            visit_type: 'Follow-up',
            priority: 'High',
          },
          {
            patient_id: 'patient-002',
            patient_name: 'Daniel Nguyen',
            time: '11:00 AM',
            status: 'Awaiting intake',
            visit_type: 'New patient',
            priority: 'Medium',
          },
          {
            patient_id: 'patient-003',
            patient_name: 'Sofia Patel',
            time: '11:30 AM',
            status: 'Lab review',
            visit_type: 'Check-in',
            priority: 'Normal',
          },
        ])
      })
  }, [])

  const dashboardCards = overview
    ? [
        { title: 'Patients today', value: overview.today_patients, detail: 'Active care list', tone: 'emerald' },
        { title: 'Appointments', value: overview.appointments_today, detail: 'Scheduled today', tone: 'blue' },
        { title: 'Pending review', value: overview.pending_reviews, detail: 'Awaiting follow-up', tone: 'violet' },
        { title: 'Avg. wait', value: overview.avg_wait_time, detail: 'Current clinic flow', tone: 'amber' },
      ]
    : []

  return (
    <div style={{ display: 'grid', gap: 24 }}>
      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 18 }}>
        {dashboardCards.map((card) => (
          <article
            key={card.title}
            style={{
              background: '#ffffff',
              border: '1px solid #e5e7eb',
              borderRadius: 18,
              boxShadow: '0 8px 24px rgba(15, 23, 42, 0.06)',
              padding: 20,
              backgroundImage: `linear-gradient(135deg, ${cardStyles[card.tone as keyof typeof cardStyles]} 0%, #ffffff 100%)`,
            }}
          >
            <div style={{ fontSize: 12, color: '#64748b', marginBottom: 8 }}>{card.title}</div>
            <div style={{ fontSize: 28, fontWeight: 700, color: '#0f172a', marginBottom: 6 }}>{card.value}</div>
            <div style={{ fontSize: 13, color: '#475569' }}>{card.detail}</div>
          </article>
        ))}
      </section>

      <section style={{ display: 'grid', gridTemplateColumns: '1.4fr 0.8fr', gap: 24 }}>
        <div style={{ background: '#fff', borderRadius: 20, border: '1px solid #e5e7eb', padding: 24 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
            <div style={{ fontWeight: 700, fontSize: 20 }}>Patient queue</div>
            <span style={{ background: '#ecfeff', color: '#155e75', borderRadius: 999, padding: '6px 10px', fontSize: 12, fontWeight: 600 }}>
              {overview?.clinic_status ?? 'On schedule'}
            </span>
          </div>

          <div style={{ display: 'grid', gap: 12 }}>
            {queue.map((patient) => (
              <div
                key={patient.patient_id}
                style={{
                  display: 'grid',
                  gridTemplateColumns: '1.3fr 0.7fr 0.7fr 0.7fr',
                  gap: 12,
                  alignItems: 'center',
                  background: '#f8fafc',
                  borderRadius: 14,
                  padding: '14px 16px',
                }}
              >
                <div>
                  <div style={{ fontWeight: 700 }}>{patient.patient_name}</div>
                  <div style={{ color: '#64748b', fontSize: 12 }}>{patient.visit_type}</div>
                </div>
                <div style={{ color: '#475569', fontWeight: 600 }}>{patient.time}</div>
                <div>
                  <span style={{ background: '#dbeafe', color: '#1d4ed8', borderRadius: 999, padding: '6px 8px', fontSize: 11, fontWeight: 700 }}>
                    {patient.status}
                  </span>
                </div>
                <div style={{ justifySelf: 'end' }}>
                  <span style={{ background: '#fef3c7', color: '#92400e', borderRadius: 999, padding: '6px 8px', fontSize: 11, fontWeight: 700 }}>
                    {patient.priority}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div style={{ background: '#fff', borderRadius: 20, border: '1px solid #e5e7eb', padding: 24 }}>
          <div style={{ fontWeight: 700, fontSize: 20, marginBottom: 16 }}>Doctor overview</div>
          {overview ? (
            <div style={{ display: 'grid', gap: 16 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                <div style={{ width: 52, height: 52, borderRadius: '50%', background: '#dbeafe', display: 'grid', placeItems: 'center', fontWeight: 700 }}>
                  {overview.name.split(' ').map((word) => word[0]).slice(0,2).join('')}
                </div>
                <div>
                  <div style={{ fontWeight: 700 }}>{overview.name}</div>
                  <div style={{ color: '#64748b', fontSize: 12 }}>{overview.specialty}</div>
                </div>
              </div>

              <div style={{ background: '#f8fafc', borderRadius: 16, padding: 16, display: 'grid', gap: 8 }}>
                <div><strong>Next round:</strong> {overview.next_round}</div>
                <div><strong>Avg wait time:</strong> {overview.avg_wait_time}</div>
                <div><strong>Patients today:</strong> {overview.today_patients}</div>
              </div>
            </div>
          ) : (
            <div>Loading doctor overview…</div>
          )}
        </div>
      </section>

      <section style={{ background: '#fff', borderRadius: 20, border: '1px solid #e5e7eb', padding: 24 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
          <div style={{ fontWeight: 700, fontSize: 20 }}>Care planning</div>
          <button style={{ border: '1px solid #dbeafe', background: '#eff6ff', color: '#1d4ed8', borderRadius: 10, padding: '10px 14px', fontWeight: 600 }}>
            Review notes
          </button>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 18 }}>
          <div style={{ background: '#f8fafc', borderRadius: 16, padding: 18 }}>
            <div style={{ fontSize: 12, color: '#64748b', marginBottom: 6 }}>Care coordination</div>
            <div style={{ fontWeight: 700, fontSize: 20 }}>6 pending</div>
            <div style={{ color: '#475569', marginTop: 8 }}>Cross-team follow-ups requiring review</div>
          </div>
          <div style={{ background: '#f8fafc', borderRadius: 16, padding: 18 }}>
            <div style={{ fontSize: 12, color: '#64748b', marginBottom: 6 }}>EHR alerts</div>
            <div style={{ fontWeight: 700, fontSize: 20 }}>3 critical</div>
            <div style={{ color: '#475569', marginTop: 8 }}>Medication and lab issues under review</div>
          </div>
          <div style={{ background: '#f8fafc', borderRadius: 16, padding: 18 }}>
            <div style={{ fontSize: 12, color: '#64748b', marginBottom: 6 }}>Next consult</div>
            <div style={{ fontWeight: 700, fontSize: 20 }}>10:30 AM</div>
            <div style={{ color: '#475569', marginTop: 8 }}>Ava Martinez · Follow-up review</div>
          </div>
        </div>
      </section>

      <AppointmentScheduler />
    </div>
  )
}
