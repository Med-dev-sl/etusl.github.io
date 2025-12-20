import React, { useState, useEffect } from 'react';
import './Hero.css';

function Hero() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const slides = [
    {
      id: 1,
      title: 'Excellence in Education',
      subtitle: 'Transforming futures through quality learning',
      image: 'https://images.unsplash.com/photo-1427504494785-cdee0fbb0d5e?w=1200&h=500&fit=crop',
      color: '#062a6f',
    },
    {
      id: 2,
      title: 'World-Class Faculty',
      subtitle: 'Expert educators dedicated to your success',
      image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=1200&h=500&fit=crop',
      color: '#1a5490',
    },
    {
      id: 3,
      title: 'Modern Campus Life',
      subtitle: 'State-of-the-art facilities and vibrant community',
      image: 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1200&h=500&fit=crop',
      color: '#0d3d7a',
    },
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 5000);
    return () => clearInterval(timer);
  }, [slides.length]);

  // fetch active announcements from backend
  const [announcements, setAnnouncements] = useState([]);
  useEffect(() => {
    let mounted = true;
    // In development the frontend server runs on a different port (3000).
    // Request the backend directly so fetch reaches the Django server.
    fetch('http://127.0.0.1:8000/api/announcements/active/')
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then((data) => {
        if (mounted) setAnnouncements(data || []);
      })
      .catch((err) => {
        // log for debugging in browser console
        // eslint-disable-next-line no-console
        console.error('Failed fetching announcements:', err);
        if (mounted) setAnnouncements([]);
      });
    return () => {
      mounted = false;
    };
  }, []);

  const goToSlide = (index) => {
    setCurrentSlide(index);
  };

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % slides.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length);
  };

  return (
    <>
    <div className="hero-carousel">
      <div className="hero-carousel__slides">
        {slides.map((slide, index) => (
          <div
            key={slide.id}
            className={`hero-slide ${index === currentSlide ? 'hero-slide--active' : ''}`}
            style={{ backgroundImage: `url(${slide.image})` }}
          >
            <div className="hero-slide__overlay" />
            <div className="hero-slide__content">
              <h1 className="hero-slide__title">{slide.title}</h1>
              <p className="hero-slide__subtitle">{slide.subtitle}</p>
              <button className="hero-slide__button">Explore More</button>
            </div>
          </div>
        ))}
      </div>

      <button className="hero-carousel__control hero-carousel__control--prev" onClick={prevSlide} aria-label="Previous slide">
        ‹
      </button>
      <button className="hero-carousel__control hero-carousel__control--next" onClick={nextSlide} aria-label="Next slide">
        ›
      </button>

      <div className="hero-carousel__indicators">
        {slides.map((_, index) => (
          <button
            key={index}
            className={`hero-carousel__dot ${index === currentSlide ? 'hero-carousel__dot--active' : ''}`}
            onClick={() => goToSlide(index)}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </div>

      {announcements && announcements.length > 0 && (
        <div className="announcement-bar" aria-live="polite">
          <div className="announcement-marquee">
            {announcements.map((a) => (
              <div className="announcement-item" key={a.id}>
                <strong>{a.title}:</strong>&nbsp;{a.body}
              </div>
            ))}
          </div>
        </div>
        )}
      </>
    );
}

export default Hero;
