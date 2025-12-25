import React, { useEffect, useState } from 'react';
import '../About.css';

export default function AffiliatesPartners() {
  const [affiliates, setAffiliates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [openIndex, setOpenIndex] = useState(null);

  useEffect(() => {
    let mounted = true;
    fetch('/api/affiliates/?ordering=order')
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then((data) => {
        if (mounted) setAffiliates(data);
      })
      .catch((err) => {
        if (mounted) setError(err.message || 'Failed to load affiliates');
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });
    return () => (mounted = false);
  }, []);

  const toggle = (i) => setOpenIndex(openIndex === i ? null : i);

  if (loading) return <div className="about-description">Loading affiliates...</div>;
  if (error) return <div className="about-description">Error: {error}</div>;

  return (
    <section className="about-section" aria-label="Affiliates and Partners">
      <div className="about-container">
        <div className="about-content">
          <header className="about-header">
            <h2 className="about-title">Affiliates &amp; Partners</h2>
          </header>

          <div className="affiliates-accordion">
            {affiliates.length === 0 && (
              <p className="about-description">No affiliates found.</p>
            )}

            {affiliates.map((a, i) => (
              <div className="affiliate-item" key={a.id}>
                <button
                  className={`affiliate-toggle ${openIndex === i ? 'open' : ''}`}
                  onClick={() => toggle(i)}
                  aria-expanded={openIndex === i}
                  aria-controls={`affiliate-panel-${a.id}`}
                >
                  <div className="affiliate-summary">
                    <div className="affiliate-name">{a.name}</div>
                    <div className="affiliate-short">{a.short_description}</div>
                  </div>
                  <div className="affiliate-icon">{openIndex === i ? '−' : '+'}</div>
                </button>

                <div
                  id={`affiliate-panel-${a.id}`}
                  className={`affiliate-panel ${openIndex === i ? 'expanded' : 'collapsed'}`}
                  role="region"
                  aria-labelledby={`affiliate-toggle-${a.id}`}
                >
                  <div className="affiliate-panel-inner">
                    {a.featured_image && (
                      <img src={a.featured_image} alt={a.name} className="affiliate-image" />
                    )}

                    <div className="affiliate-details">
                      <div
                        className="affiliate-description"
                        dangerouslySetInnerHTML={{ __html: a.description || '<p>No description.</p>' }}
                      />

                      <div className="affiliate-actions">
                        {a.website && (
                          <a href={a.website} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
                            Visit School Website
                          </a>
                        )}
                      </div>

                      <div className="affiliate-contact">
                        {a.contact_email && <div>Email: <a href={`mailto:${a.contact_email}`}>{a.contact_email}</a></div>}
                        {a.contact_phone && <div>Phone: <a href={`tel:${a.contact_phone}`}>{a.contact_phone}</a></div>}
                        {a.address && <div>Address: {a.address}</div>}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>

        </div>
      </div>
    </section>
  );
}

