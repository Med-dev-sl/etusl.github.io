import React, { useEffect, useState } from 'react';
import './Footer.css';

export default function Footer() {
  const [sections, setSections] = useState([]);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/footer-sections/?ordering=order')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => {
        const arr = Array.isArray(data) ? data : (data.results || data.items || []);
        if (mounted) setSections(arr);
      })
      .catch(() => mounted && setSections([]));
    return () => { mounted = false; };
  }, []);

  return (
    <footer className="footer">
      <div className="footer-container">
        {/* Logo & Contact Info */}
        <div className="footer-section footer-logo-section">
          <div className="footer-logo">
            <div className="logo-placeholder">🎓</div>
            <div className="footer-org-name">
              <div className="org-title">EASTERN TECHNICAL</div>
              <div className="org-title">UNIVERSITY</div>
            </div>
          </div>
          <div className="footer-contact">
            <p>+233-(0)302-213820</p>
            <p>+233-(0)302-213850</p>
            <p>pad@ug.edu.gh</p>
            <p>P. O Box LG 25 Legon-Accra</p>
          </div>
        </div>

        {/* Dynamic Footer Sections */}
        {sections.map((section) => (
          <div key={section.id} className="footer-section">
            <h3 className="footer-section-title">{section.title}</h3>
            <ul className="footer-links">
              {section.links && section.links.map((link) => (
                <li key={link.id}>
                  <a href={link.url} target="_blank" rel="noopener noreferrer">
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      {/* Bottom Bar - Social Icons & Call to Action */}
      <div className="footer-bottom">
        <div className="footer-bottom-container">
          <div className="footer-social">
            <a href="#" className="social-link" aria-label="LinkedIn">
              <i className="fab fa-linkedin-in"></i>
            </a>
            <a href="#" className="social-link" aria-label="Facebook">
              <i className="fab fa-facebook-f"></i>
            </a>
            <a href="#" className="social-link" aria-label="X">
              <i className="fab fa-x-twitter"></i>
            </a>
            <a href="#" className="social-link" aria-label="YouTube">
              <i className="fab fa-youtube"></i>
            </a>
            <a href="#" className="social-link" aria-label="TikTok">
              <i className="fab fa-tiktok"></i>
            </a>
            <a href="#" className="social-link" aria-label="Instagram">
              <i className="fab fa-instagram"></i>
            </a>
          </div>
          <button className="footer-cta-btn">GIVE TO ETU</button>
        </div>
      </div>
    </footer>
  );
}
