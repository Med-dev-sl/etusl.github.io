import React, { useState, useEffect } from 'react';
import './Hero.css';
import About from './About';
import Faculty from './Faculty';

function Hero() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [announcements, setAnnouncements] = useState([]);
  const [events, setEvents] = useState([]);

  const slides = [
    { id: 1, title: 'Excellence in Education', subtitle: 'Transforming futures through quality learning', image: 'https://images.unsplash.com/photo-1427504494785-cdee0fbb0d5e?w=1200&h=500&fit=crop' },
    { id: 2, title: 'World-Class Faculty', subtitle: 'Expert educators dedicated to your success', image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=1200&h=500&fit=crop' },
    { id: 3, title: 'Modern Campus Life', subtitle: 'State-of-the-art facilities and vibrant community', image: 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1200&h=500&fit=crop' },
  ];

  useEffect(() => {
    const timer = setInterval(() => setCurrentSlide((s) => (s + 1) % slides.length), 5000);
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/announcements/active/')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => mounted && setAnnouncements(data || []))
      .catch(() => mounted && setAnnouncements([]));
    return () => { mounted = false; };
  }, []);

  useEffect(() => {
    let mounted = true;
    fetch('http://127.0.0.1:8000/api/events/?ordering=-created_at')
      .then((r) => (r.ok ? r.json() : Promise.reject(r.statusText)))
      .then((data) => mounted && setEvents((Array.isArray(data) ? data.slice(0, 4) : [])))
      .catch(() => mounted && setEvents([]));
    return () => { mounted = false; };
  }, []);

  const formatDate = (isoOrDate) => {
    if (!isoOrDate) return '';
    try {
      const d = new Date(isoOrDate);
      return d.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' });
    } catch (e) {
      return isoOrDate;
    }
  };

  return (
    <>
      <div className="hero-carousel">
        <div className="hero-carousel__slides">
          {slides.map((slide, index) => (
            <div key={slide.id} className={`hero-slide ${index === currentSlide ? 'hero-slide--active' : ''}`} style={{ backgroundImage: `url(${slide.image})` }}>
              <div className="hero-slide__overlay" />
              <div className="hero-slide__content">
                <h1 className="hero-slide__title">{slide.title}</h1>
                <p className="hero-slide__subtitle">{slide.subtitle}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {announcements && announcements.length > 0 && (
        <div className="announcement-bar" aria-live="polite">
          <div className="announcement-single">
            <strong className="announcement-single__title">{announcements[0].title}</strong>
            <span className="announcement-single__body">{announcements[0].body}</span>
          </div>
        </div>
      )}

      <About />
      <Faculty />

      <section className="events-section" aria-label="Upcoming events">
        <div className="events-header">
          <h2 className="events-title">Events AT Eastern Technical University</h2>
          <a className="events-viewall" href="/events" title="View all events">View all events <span className="events-arrow">→</span></a>
        </div>

        <div className="events-container">
          {events.map((e, i) => (
            <article className={`event-card slide-in`} key={e.id} style={{ animationDelay: `${i * 80}ms` }}>
              <div className="event-photo" style={{ backgroundImage: e.photo ? `url(${e.photo})` : 'none', backgroundColor: '#f5f5f5' }} />
              <div className="event-content">
                <div className="event-topline">
                  <span className="event-org">Eastern Technical University</span>
                  {(e.event_date || e.created_at) && (
                    <span className="event-date-wrapper">
                      <svg className="event-date-icon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M19 4h-1V2h-2v2H8V2H6v2H5a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 14H5V9h14v9zM7 11h5v5H7z"/></svg>
                      <time className="event-date" dateTime={e.event_date || e.created_at}>{formatDate(e.event_date || e.created_at)}</time>
                    </span>
                  )}
                </div>
                <h3 className="event-title">{e.name}</h3>
                <p className="event-desc">{e.description ? (e.description.length > 120 ? `${e.description.slice(0, 117)}…` : e.description) : ''}</p>
                <div className="event-meta">
                  <span className="event-meta-item"><svg className="event-meta-icon" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg><span className="meta-text">{e.location || 'TBA'}</span></span>
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>
    </>
  );
}

export default Hero;
        


