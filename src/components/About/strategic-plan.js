import React from 'react';
import '../About.css';
import StrategicPlanContent from './StrategicPlanContent';

export default function StrategicPlan() {
	return (
		<main>
			<section className="about-section strategic-hero" aria-label="Strategic Plan">
				<div className="strategic-hero__bg" />
				<div className="strategic-hero__overlay" />
				<div className="strategic-hero__caption">
					<h1 className="hero-title">2018-2025 <strong>STRATEGIC PLAN</strong></h1>
					<p className="hero-subtitle">WHAT MUST BE DONE</p>
				</div>
			</section>

			<StrategicPlanContent />
		</main>
	);
}

