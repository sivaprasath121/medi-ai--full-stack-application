export type AppRole = 'patient' | 'doctor'

type RoleSwitcherProps = {
  value: AppRole
  onChange: (role: AppRole) => void
}

export function RoleSwitcher({ value, onChange }: RoleSwitcherProps) {
  const options: { label: string; value: AppRole }[] = [
    { label: 'Patient view', value: 'patient' },
    { label: 'Doctor view', value: 'doctor' },
  ]

  return (
    <div
      style={{
        display: 'inline-flex',
        background: '#e2e8f0',
        borderRadius: 999,
        padding: 6,
        gap: 6,
      }}
    >
      {options.map((option) => {
        const selected = value === option.value
        return (
          <button
            key={option.value}
            onClick={() => onChange(option.value)}
            style={{
              border: 'none',
              borderRadius: 999,
              background: selected ? '#0f172a' : 'transparent',
              color: selected ? '#fff' : '#334155',
              padding: '10px 16px',
              fontWeight: 700,
              cursor: 'pointer',
            }}
          >
            {option.label}
          </button>
        )
      })}
    </div>
  )
}
