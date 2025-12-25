import React, { useEffect, useState } from 'react';
import '../About.css';

export default function StrategicPriorities() {
	const [priority, setPriority] = useState(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	const [visible, setVisible] = useState(false);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch('http://127.0.0.1:8000/api/strategic-priorities/');
				if (!response.ok) throw new Error('Failed to fetch');
				const result = await response.json();
				const priorityData = Array.isArray(result) ? result[0] : (result.results?.[0] || result);
				setPriority(priorityData);
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

		const section = document.getElementById('strategic-priorities-section');
		if (section) observer.observe(section);

		return () => observer.disconnect();
	}, [priority]);

	if (loading) return <div style={{ textAlign: 'center', padding: '40px' }}>Loading...</div>;
	if (error) return <div style={{ textAlign: 'center', padding: '40px' }}>Error: {error}</div>;
	if (!priority) return null;

	return (
		<section 
			id="strategic-priorities-section"
			className="strategic-priorities-section"
			style={{
				opacity: visible ? 1 : 0,
				transform: visible ? 'translateY(0)' : 'translateY(60px)',
				transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1)',
			}}
		>
			<div className="strategic-priorities-container">
				<div className="strategic-priorities-grid">
					{/* Left Column: Image */}
					{priority.featured_image && (
						<div 
							className="strategic-priorities-left"
							style={{
								opacity: visible ? 1 : 0,
								transform: visible ? 'translateX(0)' : 'translateX(-40px)',
								transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s',
							}}
						>
							<img 
								src={priority.featured_image} 
								alt={priority.image_alt || 'Strategic Priorities'} 
								className="strategic-priorities-image"
							/>
						</div>
					)}

					{/* Right Column: Content */}
					<div 
						className="strategic-priorities-right"
						style={{
							opacity: visible ? 1 : 0,
							transform: visible ? 'translateX(0)' : 'translateX(40px)',
							transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s',
						}}
					>
						<div className="strategic-priorities-box">
							<h2 className="strategic-priorities-title">{priority.title}</h2>
							{priority.items && priority.items.length > 0 && (
								<ul className="strategic-priorities-list">
									{priority.items.map((item) => (
										<li key={item.id} className="priority-item">
											{item.text}
										</li>
									))}
								</ul>
							)}
						</div>
					</div>
				</div>
			</div>
		</section>
	);
}
