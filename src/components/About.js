import React, { useState, useEffect } from 'react';
import './About.css';

function About() {
  const [about, setAbout] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/aboutuniversity/')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => {
        if (mounted) {
          const aboutData = Array.isArray(data) ? data[0] : data;
          setAbout(aboutData);
          setLoading(false);
        }
      })
      .catch(() => {
        if (mounted) {
          setLoading(false);
        }
      });
    return () => { mounted = false; };
  }, []);

  if (loading || !about) {
    return null;
  }

  return (
    <section className="about-section" aria-label="About Eastern Technical University">
      <div className="about-container">
        <div className="about-image-wrapper">
          {about.image && (
            <img 
              src={about.image} 
              alt={about.heading}
              className="about-image"
            />
          )}
          <div className="about-image-overlay" />
        </div>

        <div className="about-content">
          <div className="about-header">
            <h2 className="about-title">{about.heading}</h2>
            <div className="about-title-underline" />
          </div>

          <p className="about-description">
            {about.description}
          </p>

          <div className="about-accent" />
        </div>
      </div>
    </section>
  );
}

export default About;
