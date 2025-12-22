import React, { useEffect, useState } from 'react';
import './Faculty.css';

// Inline material-like SVG icons for different faculty types
function Icon({ type }) {
  const icons = {
    engineering: (
      <svg className="faculty-icon-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M22.7 13.35l-2.11-.36a7.97 7.97 0 0 0-.53-1.28l1.23-1.63a1 1 0 0 0-.15-1.34l-1.41-1.41a1 1 0 0 0-1.34-.15l-1.63 1.23c-.41-.2-.84-.36-1.28-.53l-.36-2.11A1 1 0 0 0 13.9 2h-3.8a1 1 0 0 0-.99.84l-.36 2.11c-.44.17-.87.33-1.28.53L5.64 4.25a1 1 0 0 0-1.34.15L2.9 5.81a1 1 0 0 0-.15 1.34l1.23 1.63c-.2.41-.36.84-.53 1.28l-2.11.36A1 1 0 0 0 0 11.1v3.8a1 1 0 0 0 .84.99l2.11.36c.17.44.33.87.53 1.28l-1.23 1.63a1 1 0 0 0 .15 1.34l1.41 1.41c.39.39 1.01.5 1.49.27l1.63-1.23c.41.2.84.36 1.28.53l.36 2.11c.08.47.48.84.99.84h3.8c.51 0 .91-.37.99-.84l.36-2.11c.44-.17.87-.33 1.28-.53l1.63 1.23c.48.23 1.1.12 1.49-.27l1.41-1.41a1 1 0 0 0 .15-1.34l-1.23-1.63c.2-.41.36-.84.53-1.28l2.11-.36a1 1 0 0 0 .84-.99v-3.8a1 1 0 0 0-.3-.74zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8z"/></svg>
    ),
    science: (
      <svg className="faculty-icon-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13 10V3h-2v7H3v2h8v7h2v-7h8v-2z"/></svg>
    ),
    business: (
      <svg className="faculty-icon-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 8h14v-2H7v2zm0-4h14v-2H7v2zm0-6v2h14V7H7z"/></svg>
    ),
    arts: (
      <svg className="faculty-icon-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2l4 4-4 4-4-4 4-4zm0 6l4 4-4 4-4-4 4-4zm0 6l4 4-4 4-4-4 4-4z"/></svg>
    ),
    default: (
      <svg className="faculty-icon-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-4 0-8 2-8 6v2h16v-2c0-4-4-6-8-6z"/></svg>
    )
  };
  return icons[type] || icons.default;
}

function pickIconType(name) {
  if (!name) return 'default';
  const n = name.toLowerCase();
  if (n.includes('engineer')) return 'engineering';
  if (n.includes('science') || n.includes('technology') || n.includes('research')) return 'science';
  if (n.includes('business') || n.includes('commerce') || n.includes('management')) return 'business';
  if (n.includes('art') || n.includes('design') || n.includes('creative') || n.includes('humanities')) return 'arts';
  return 'default';
}

export default function Faculty() {
  const [faculties, setFaculties] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/faculties/')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => {
        if (!mounted) return;
        const list = Array.isArray(data) ? data : (data.results || []);
        setFaculties(list);
        setLoading(false);
      })
      .catch(() => {
        if (mounted) {
          setFaculties([]);
          setLoading(false);
        }
      });
    return () => { mounted = false; };
  }, []);

  if (loading) return null;
  if (!faculties || faculties.length === 0) return null;

  return (
    <section className="faculty-section" aria-label="Faculties">
      <h3 className="faculty-section-title">Faculties</h3>
      <div className="faculty-grid">
        {faculties.map((f) => (
          <div className="faculty-card" key={f.id}>
            <div className="faculty-card-icon">
              <Icon type={pickIconType(f.name)} />
            </div>
            <div className="faculty-card-body">
              <h4 className="faculty-name">{f.name}</h4>
              <p className="faculty-desc">{f.description ? (f.description.length > 160 ? `${f.description.slice(0,157)}…` : f.description) : ''}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
