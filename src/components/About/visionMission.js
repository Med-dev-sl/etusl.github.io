import React, { useEffect, useState } from 'react';
import '../About.css';

export default function VisionMission() {
	const [data, setData] = useState(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	const [visible, setVisible] = useState(false);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch('http://127.0.0.1:8000/api/vision-mission/');
				if (!response.ok) throw new Error('Failed to fetch');
				const result = await response.json();
				const visionData = Array.isArray(result) ? result[0] : result;
				setData(visionData);
			} catch (err) {
				setError(err.message);
				console.error(err);
			} finally {
				setLoading(false);
			}
		};

		fetchData();
	}, []);

	useEffect(() => {
		const observer = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					setVisible(true);
					observer.unobserve(entry.target);
				}
			});
		}, { threshold: 0.15 });

		const section = document.getElementById('vision-mission-section');
		if (section) observer.observe(section);

		return () => observer.disconnect();
	}, [data]);

	if (loading) return <div style={{ textAlign: 'center', padding: '40px' }}>Loading...</div>;
	if (error) return <div style={{ textAlign: 'center', padding: '40px' }}>Error: {error}</div>;
	if (!data) return null;

	return (
		<section 
			id="vision-mission-section"
			className="vision-mission-section"
			style={{
				opacity: visible ? 1 : 0,
				transform: visible ? 'translateY(0)' : 'translateY(60px)',
				transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1)',
			}}
		>
			<div className="vision-mission-container">
				<h2 className="vision-mission-heading">Mission and Vision</h2>
				
				<div className="vision-mission-grid">
					{/* Left Column: Text Content */}
					<div 
						className="vision-mission-left"
						style={{
							opacity: visible ? 1 : 0,
							transform: visible ? 'translateX(0)' : 'translateX(-40px)',
							transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s',
						}}
					>
						<div className="vision-mission-box">
							<h3 className="vision-mission-title">{data.vision_title}</h3>
							<p className="vision-mission-text">{data.vision_text}</p>

							<h3 className="vision-mission-title">{data.mission_title}</h3>
							<p className="vision-mission-text">{data.mission_text}</p>
						</div>
					</div>

					{/* Right Column: Image */}
					{data.featured_image && (
						<div 
							className="vision-mission-right"
							style={{
								opacity: visible ? 1 : 0,
								transform: visible ? 'translateX(0)' : 'translateX(40px)',
								transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s',
							}}
						>
							<img 
								src={data.featured_image} 
								alt={data.image_alt || 'Vision and Mission'} 
								className="vision-mission-image"
							/>
						</div>
					)}
				</div>
			</div>
		</section>
	);
}

