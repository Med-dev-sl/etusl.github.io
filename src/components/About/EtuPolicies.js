import React, { useEffect, useState } from 'react';
import '../About.css';

export default function EtuPolicies() {
  const [policies, setPolicies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const heroImage = `${process.env.PUBLIC_URL || ''}/static/images/policies-hero.jpg`;

  useEffect(() => {
    let mounted = true;
    fetch('/api/policies/?ordering=order')
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then((data) => {
        if (mounted) setPolicies(data);
      })
      .catch((err) => {
        if (mounted) setError(err.message || 'Failed to load policies');
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });
    return () => (mounted = false);
  }, []);

  return (
    <main>
      <section
        className="about-hero policies-hero"
        aria-label="ETU Policies hero"
        style={{ backgroundImage: `url(${heroImage})` }}
      >
        <div className="hero-overlay" />
        <div className="hero-content">
          <h1 className="hero-title">ETU Policies</h1>
          <p className="hero-subtitle">Policies, guidelines and governance documents for the University</p>
        </div>
      </section>

      <section className="about-section" aria-label="ETU Policies">
        <div className="about-container">
          <div className="about-content">
            <header className="about-header">
              <h2 className="about-title">Policies &amp; Documents</h2>
            </header>

            {loading && <p className="about-description">Loading policies...</p>}
            {error && <p className="about-description">Error: {error}</p>}

            {!loading && !error && (
              <div className="policies-grid">
                {policies.length === 0 ? (
                  <p className="about-description">No policies available at the moment.</p>
                ) : (
                  policies.map((policy) => (
                    <div className="policy-card" key={policy.id}>
                      <div className="policy-card-content">
                        <div className="policy-card-inner">
                          <h3 className="policy-title">{policy.title}</h3>
                          {policy.short_description && (
                            <p className="policy-description">{policy.short_description}</p>
                          )}
                          <div className="policy-actions">
                            {policy.file_url && (
                              <a
                                href={policy.file_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="policy-download-btn"
                                download
                              >
                                Download
                              </a>
                            )}
                          </div>
                        </div>
                      </div>
                      <div className="policy-card-image-left">
                        <div className="policy-image-wrapper">
                          {policy.image_url ? (
                            <img src={policy.image_url} alt={policy.title} className="policy-image" />
                          ) : (
                            <div className="policy-image-placeholder">
                              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M9 5H5c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2h-4l-2-2z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                              </svg>
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                  ))
                )}
              </div>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}

