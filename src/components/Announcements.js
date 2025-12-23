import React, { useEffect, useState } from 'react';
import './Announcements.css';

function formatDate(isoOrDate) {
  if (!isoOrDate) return '';
  try {
    const d = new Date(isoOrDate);
    return d.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
  } catch (e) {
    return isoOrDate;
  }
}

export default function Announcements() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/announcements/?ordering=-date,-created_at')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => {
        const arr = Array.isArray(data) ? data : (data.results || data.items || []);
        if (mounted) setItems(arr);
      })
      .catch(() => mounted && setItems([]));
    return () => { mounted = false; };
  }, []);

  return (
    <section className="announcements-grid" aria-label="Announcements and Featured Links">
      <div className="announcements-column">
        <h3 className="announcements-heading">Announcements</h3>
        <div className="announcements-list">
          {items.map((a) => (
            <article key={a.id} className="announcement-item">
              <h4 className="announcement-item__title">{a.title}</h4>
              {a.date && <div className="announcement-item__date">{formatDate(a.date)}</div>}
              <hr />
            </article>
          ))}
          <div className="announcements-more">
            <a className="announcements-more__btn" href="/announcements">Explore more announcements</a>
          </div>
        </div>
      </div>

      <aside className="featured-column">
        <h3 className="featured-heading">Featured Links</h3>
        <ul className="featured-list">
          {items.filter(a => a.is_featured).length === 0 && (
            <li className="featured-empty">No featured links yet. </li>
          )}
          {items.filter(a => a.is_featured).map((a) => (
            <li key={a.id}>
              <a href={`/announcements/${a.id}`}>{a.title}</a>
            </li>
          ))}
        </ul>
      </aside>
    </section>
  );
}
