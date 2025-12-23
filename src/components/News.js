import React, { useEffect, useState } from 'react';
import './News.css';

function News() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/news/?ordering=-date,-created_at')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => mounted && setNews(Array.isArray(data) ? data : []))
      .catch(() => mounted && setNews([]));
    return () => { mounted = false; };
  }, []);

  const [plan, setPlan] = useState(null);
  useEffect(() => {
    let mounted = true;
    // fetch the latest strategic plan (most recent)
    fetch('http://127.0.0.1:8000/api/strategic-plans/?ordering=-created_at')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => {
        if (!mounted) return;
        // DRF may return paginated response: { results: [...] }
        const items = Array.isArray(data) ? data : (data.results || data.items || []);
        if (Array.isArray(items) && items.length > 0) setPlan(items[0]);
        else setPlan(null);
      })
      .catch(() => mounted && setPlan(null));
    return () => { mounted = false; };
  }, []);

  const formatDate = (isoOrDate) => {
    if (!isoOrDate) return '';
    try {
      const d = new Date(isoOrDate);
      return d.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
    } catch (e) { return isoOrDate; }
  };

  if (!news || news.length === 0) return null;

  const [featured, ...others] = news;

  return (
    <>
      <section className="news-section" aria-label="News">
        <div className="news-grid">
          <div className="news-featured">
          {featured.image && (
            <div className="news-featured__image" style={{ backgroundImage: `url(${featured.image})` }} />
          )}
          <div className="news-featured__content">
            <time className="news-featured__date">{formatDate(featured.date || featured.created_at)}</time>
            <h3 className="news-featured__title">{featured.heading}</h3>
            <p className="news-featured__excerpt">{featured.description ? (featured.description.length > 220 ? `${featured.description.slice(0, 217)}…` : featured.description) : ''}</p>
          </div>
        </div>

        <aside className="news-side">
          <div className="news-side__header">
            <h4 className="news-side__title">Explore more news</h4>
            <a className="news-side__cta" href="/news">GO <span className="news-side__cta-arrow">›</span></a>
          </div>

          <div className="news-list">
            {others.map((n) => (
              <article key={n.id} className="news-list-item">
                <h5 className="news-list-item__title">{n.heading}</h5>
                <p className="news-list-item__excerpt">{n.description ? (n.description.length > 140 ? `${n.description.slice(0, 137)}…` : n.description) : ''}</p>
                <time className="news-list-item__date">{formatDate(n.date || n.created_at)}</time>
                <hr />
              </article>
            ))}
          </div>
        </aside>
        </div>
      </section>
      {plan && (
        <section className="strategic-hero" aria-label="Strategic Plan">
          {plan.main_image && <div className="strategic-hero__bg" style={{ backgroundImage: `url(${plan.main_image})` }} />}
          <div className="strategic-hero__overlay" />
          <div className="strategic-hero__content">
            <h2 className="strategic-hero__title">{plan.title || "Strategic Plan"}</h2>
            {plan.summary && <p className="strategic-hero__subtitle">{plan.summary}</p>}
            <a className="strategic-hero__cta" href={`/strategic-plans/${plan.id || ''}`}>Find out more</a>
          </div>
        </section>
      )}
    </>
  );
}

export default News;
