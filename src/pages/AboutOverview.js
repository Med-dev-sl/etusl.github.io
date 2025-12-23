import React from 'react';
import '../components/About/About.css';

export default function AboutOverview() {
  return (
    <main>
      <section className="about-section" aria-label="Overview">
        <div className="about-container">
          <div className="about-content">
            <header className="about-header">
              <h2 className="about-title">Overview</h2>
            </header>
            <div className="about-description">
              <p>
                Eastern Technical University (ETU) is committed to providing high-quality technical and
                professional education. This overview is a placeholder — replace with admin-driven content
                or detailed static copy as needed.
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
