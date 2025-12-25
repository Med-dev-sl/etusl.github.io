import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './MainHeader.css';

function MainHeader() {
  const [mobileOpen, setMobileOpen] = useState(false);

  const toggleMobile = () => setMobileOpen((s) => !s);

  // lock body scroll while mobile menu is open
  useEffect(() => {
    if (mobileOpen) {
      // save current overflow to restore later
      const prev = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.overflow = prev || '';
      };
    }
    // ensure overflow restored when mobileOpen false
    document.body.style.overflow = '';
    return undefined;
  }, [mobileOpen]);

  return (
    <header className="main-header">
      <div className="main-header__inner">
        <button
          className={`menu__hamburger ${mobileOpen ? 'is-open' : ''}`}
          onClick={toggleMobile}
          aria-label="Toggle navigation"
          aria-expanded={mobileOpen}
        >
          <span className="hamburger__box">
            <span className="hamburger__inner" />
          </span>
        </button>

        <nav className="main-header__nav" aria-label="Main Navigation">
          <ul className="menu">
            <li className="menu__item"><Link to="/">Home</Link></li>

            <li className="menu__item menu__item--has-dropdown">
              <span>About</span>
              <ul className="dropdown">
                <li><Link to="/about/overview">Overview</Link></li>
                <li><Link to="/about/history">History</Link></li>
                <li><Link to="/about/vision-mission">Vision &amp; Mission</Link></li>
                <li><Link to="/about/leadership">Leadership &amp; Directorates</Link></li>
                <li><Link to="/about/affiliates">Affiliates &amp; Partners</Link></li>
                <li><Link to="/about/strategic-plan">Strategic Plan</Link></li>
                <li><Link to="/about/policies">ETU Policies</Link></li>
              </ul>
            </li>

            <li className="menu__item menu__item--has-dropdown">
              <span>Academics</span>
              <ul className="dropdown">
                <li><Link to="/academics/overview">Overview</Link></li>
                <li><Link to="/academics/faculties">Faculties</Link></li>
                <li><Link to="/academics/programmes">Programmes</Link></li>
                <li><Link to="/academics/calendar">Academic Calendar</Link></li>
                <li><Link to="/academics/library">Library</Link></li>
              </ul>
            </li>

            <li className="menu__item menu__item--has-dropdown">
              <a href="#">Admissions</a>
              <ul className="dropdown">
                <li><a href="#">Overview</a></li>
                <li><a href="#">Undergraduate</a></li>
                <li><a href="#">Post-Graduate</a></li>
                <li><a href="#">International</a></li>
              </ul>
            </li>

            {/* centered logo placed between Admissions and Research */}
            <li className="menu__logo" aria-hidden>
              <img src="logo512.png" alt="" className="logo-image" />
            </li>

            <li className="menu__item menu__item--has-dropdown">
              <a href="#">Research</a>
              <ul className="dropdown">
                <li><a href="#">Overview</a></li>
                <li><a href="#">Ongoing Research</a></li>
                <li><a href="#">Completed Research</a></li>
              </ul>
            </li>

            <li className="menu__item menu__item--has-dropdown">
              <a href="#">News &amp; Events</a>
              <ul className="dropdown">
                <li><a href="#">Live Events</a></li>
                <li><a href="#">News &amp; Articles</a></li>
              </ul>
            </li>

            <li className="menu__item menu__item--has-dropdown">
              <a href="#">Quick Links</a>
              <ul className="dropdown">
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
                <li><a href="#">Link 3</a></li>
              </ul>
            </li>
          </ul>
        </nav>

        {/* Mobile slide-out menu */}
        <div className={`mobile-nav ${mobileOpen ? 'mobile-nav--open' : ''}`} role="dialog" aria-hidden={!mobileOpen}>
          <div className="mobile-nav__inner">
            <button className="mobile-nav__close" onClick={toggleMobile} aria-label="Close menu">×</button>
            <ul className="mobile-menu">
              <li><Link to="/" onClick={() => setMobileOpen(false)}>Home</Link></li>
              <li><Link to="/about/overview" onClick={() => setMobileOpen(false)}>About</Link></li>
              <li><Link to="/academics/overview" onClick={() => setMobileOpen(false)}>Academics</Link></li>
              <li><a href="#" onClick={() => setMobileOpen(false)}>Admissions</a></li>
              <li className="mobile-menu__logo"><img src="logo512.png" alt="" className="logo-image"/></li>
              <li><a href="#" onClick={() => setMobileOpen(false)}>Research</a></li>
              <li><a href="#" onClick={() => setMobileOpen(false)}>News &amp; Events</a></li>
              <li><a href="#" onClick={() => setMobileOpen(false)}>Quick Links</a></li>
            </ul>
          </div>
        </div>
      </div>
    </header>
  );
}

export default MainHeader;
