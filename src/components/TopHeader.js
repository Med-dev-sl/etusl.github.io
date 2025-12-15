import React from 'react';
import './TopHeader.css';

function TopHeader() {
  return (
    <div className="top-header">
      <div className="top-header__inner">
        <div className="top-header__left">
          <svg className="top-header__icon" width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 110-5 2.5 2.5 0 010 5z" fill="currentColor"/>
          </svg>
          <span className="top-header__location">Combema Road , Kenema City</span>
        </div>

        <div className="top-header__center">
          <span className="top-header__sep">•</span>
          <span className="top-header__phone">
            <svg className="top-header__icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
              <path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 01.95-.27c1.02.26 2.12.4 3.25.4a1 1 0 011 1V20a1 1 0 01-1 1C10.07 21 3 13.93 3 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.13.14 2.23.4 3.25a1 1 0 01-.27.95l-2.01 2.59z" fill="currentColor"/>
            </svg>
            <a className="top-header__link" href="tel:+1234567890">+232 (78) 231363</a>
          </span>
        </div>

        <div className="top-header__right">
          <svg className="top-header__icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
            <path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="currentColor"/>
          </svg>
          <a className="top-header__link" href="mailto:you@example.com">registrar@etusl.edu.sl</a>
        </div>
      </div>
    </div>
  );
}

export default TopHeader;
