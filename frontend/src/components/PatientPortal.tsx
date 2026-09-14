import { useEffect, useState } from 'react';
import { AppointmentScheduler } from './AppointmentScheduler';
import { patientDashboard, patientTimeline, labHistory } from '../lib/demo-data';
import type { PatientProfile as PatientProfileType } from '../types';

const cardStyles = {
  emerald: 'rgba(16,185,129,0.1)',
  blue: 'rgba(59,130,246,0.1)',
  violet: 'rgba(139,92,246,0.1)',
  amber: 'rgba(245,158,11,0.1)',
  sky: 'rgba(14,165,233,0.1)',
  rose: 'rgba(244,63,94,0.1)',
};

export function PatientPortal() {
  const [profile, setProfile] = useState<PatientProfileType | null>(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/patients/patient-001')
      .then((res) => res.json())
      .then((data) => setProfile(data))
      .catch(() => setProfile({
        id: 'patient-001',
        patient_id: 'PT-1001',
        first_name: 'Ava',
        last_name: 'Martinez',
        email: 'ava.martinez@example.com',
        phone: '555-0134',
        date_of_birth: '1995-04-18',
        gender: 'Female',
        address: '1480 Harbor Lane, Seattle, WA',
        emergency_contact: {
          name: 'Luis Martinez',
          relationship: 'Spouse',
          phone: '555-0140',
        },
        allergies: ['Penicillin', 'Peanuts'],
        current_medications: ['Vitamin D', 'Levothyroxine'],
        previous_conditions: ['Seasonal allergies'],
        surgical_history: ['Appendectomy (2018)'],
        family_history: ['Mother: hypertension', 'Father: type 2 diabetes'],
        insurance: {
          provider: 'BlueCross Demo Plan',
          member_id: 'BC-889122',
          plan_type: 'PPO',
        },
        summary: {
          upcoming_appointment: 'Cardiology follow-up | Tue 10:30 AM',
          current_medications_count: 2,
          last_lab_result: 'CBC within normal range',
          risk_level: 'Low',
        },
      }));
  }, []);

  const dashboardCards = [
    { ...patientDashboard.upcomingAppointment, tone: 'emerald' },
    { ...patientDashboard.medications, tone: 'blue' },
    { ...patientDashboard.prescriptions, tone: 'violet' },
    { ...patientDashboard.healthSummary, tone: 'amber' },
    { ...patientDashboard.labResults, tone: 'sky' },
    { ...patientDashboard.messages, tone: 'rose' },
  ];

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
          <div style={{ fontWeight: 700, fontSize: 20, marginBottom: 16 }}>Medical record timeline</div>
          <div style={{ display: 'grid', gap: 16 }}>
            {patientTimeline.map((item) => (
              <div key={`${item.date}-${item.event}`} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                <div style={{ width: 10, height: 10, borderRadius: 999, background: '#10b981' }} />
                <div style={{ flex: 1 }}>
                  <div style={{ fontSize: 13, color: '#64748b' }}>{item.date}</div>
                  <div style={{ fontWeight: 600 }}>{item.event}</div>
                </div>
                <span style={{ fontSize: 11, color: '#0f172a', background: '#f1f5f9', padding: '6px 8px', borderRadius: 999 }}>{item.kind}</span>
              </div>
            ))}
          </div>
        </div>

        <div style={{ background: '#fff', borderRadius: 20, border: '1px solid #e5e7eb', padding: 24 }}>
          <div style={{ fontWeight: 700, fontSize: 20, marginBottom: 16 }}>AI health assistant</div>
          <div style={{ background: '#f8fafc', borderRadius: 16, padding: 16, color: '#334155' }}>
            <div style={{ fontWeight: 700, marginBottom: 8 }}>MediAI Assistant</div>
            <p style={{ margin: 0, lineHeight: 1.6 }}>
              AI-generated information is for informational and decision-support purposes only. It is not a diagnosis and does not replace a qualified healthcare professional.
            </p>
          </div>
        </div>
      </section>

      <section style={{ background: '#fff', borderRadius: 20, border: '1px solid #e5e7eb', padding: 24 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
          <div style={{ fontWeight: 700, fontSize: 20 }}>Patient profile</div>
          <button style={{ border: '1px solid #dbeafe', background: '#eff6ff', color: '#1d4ed8', borderRadius: 10, padding: '10px 14px', fontWeight: 600 }}>Edit profile</button>
        </div>

        {profile ? (
          <div style={{ display: 'grid', gap: 18 }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 16 }}>
              <div><div style={{ color: '#64748b', fontSize: 12 }}>Full name</div><div style={{ fontWeight: 600 }}>{profile.first_name} {profile.last_name}</div></div>
              <div><div style={{ color: '#64748b', fontSize: 12 }}>Date of birth</div><div style={{ fontWeight: 600 }}>{profile.date_of_birth}</div></div>
              <div><div style={{ color: '#64748b', fontSize: 12 }}>Gender</div><div style={{ fontWeight: 600 }}>{profile.gender}</div></div>
              <div><div style={{ color: '#64748b', fontSize: 12 }}>Phone</div><div style={{ fontWeight: 600 }}>{profile.phone}</div></div>
              <div><div style={{ color: '#64748b', fontSize: 12 }}>Email</div><div style={{ fontWeight: 600 }}>{profile.email}</div></div>
              <div><div style={{ color: '#64748b', fontSize: 12 }}>Address</div><div style={{ fontWeight: 600 }}>{profile.address}</div></div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 18 }}>
              <div style={{ background: '#f8fafc', borderRadius: 16, padding: 16 }}>
                <div style={{ fontWeight: 700, marginBottom: 8 }}>Emergency contact</div>
                <div>{profile.emergency_contact.name}</div>
                <div style={{ color: '#64748b' }}>{profile.emergency_contact.relationship}</div>
                <div>{profile.emergency_contact.phone}</div>
              </div>

              <div style={{ background: '#f8fafc', borderRadius: 16, padding: 16 }}>
                <div style={{ fontWeight: 700, marginBottom: 8 }}>Medical information</div>
                <div style={{ color: '#475569' }}>Allergies: {profile.allergies.join(', ')}</div>
                <div style={{ color: '#475569' }}>Current medications: {profile.current_medications.join(', ')}</div>
              </div>

              <div style={{ background: '#f8fafc', borderRadius: 16, padding: 16 }}>
                <div style={{ fontWeight: 700, marginBottom: 8 }}>Insurance</div>
                <div>{profile.insurance.provider}</div>
                <div style={{ color: '#475569' }}>{profile.insurance.plan_type} · {profile.insurance.member_id}</div>
              </div>
            </div>
          </div>
        ) : (
          <div>Loading patient profile…</div>
        )}
      </section>

      <section style={{ background: '#fff', borderRadius: 20, border: '1px solid #e5e7eb', padding: 24 }}>
        <div style={{ fontWeight: 700, fontSize: 20, marginBottom: 16 }}>Lab results</div>
        <div style={{ height: 220, display: 'flex', alignItems: 'end', gap: 16 }}>
          {labHistory.map((bar) => (
            <div key={bar.date} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
              <div style={{ width: '100%', background: '#dbeafe', borderRadius: 12, height: `${bar.value * 30}px`, minHeight: 40 }} />
              <div style={{ fontSize: 12, color: '#64748b' }}>{bar.date}</div>
            </div>
          ))}
        </div>
      </section>

      <AppointmentScheduler />
    </div>
  );
}
