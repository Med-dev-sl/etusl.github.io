import React, { useEffect, useState } from 'react';
import '../About.css';

export default function CoreValues() {
	const [values, setValues] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	const [visible, setVisible] = useState(false);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch('http://127.0.0.1:8000/api/core-values/');
				if (!response.ok) throw new Error('Failed to fetch');
				const result = await response.json();
				setValues(Array.isArray(result) ? result : (result.results || []));
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

		const section = document.getElementById('core-values-section');
		if (section) observer.observe(section);

		return () => observer.disconnect();
	}, [values]);

	if (loading) return <div style={{ textAlign: 'center', padding: '40px' }}>Loading...</div>;
	if (error) return <div style={{ textAlign: 'center', padding: '40px' }}>Error: {error}</div>;

	return (
		<section 
			id="core-values-section"
			className="core-values-section"
			style={{
				opacity: visible ? 1 : 0,
				transform: visible ? 'translateY(0)' : 'translateY(60px)',
				transition: 'all 0.9s cubic-bezier(0.34, 1.56, 0.64, 1)',
			}}
		>
			<div className="core-values-container">
				<div className="core-values-header">
					<h2 className="core-values-title">Our Core Values</h2>
					<div className="core-values-divider" />
				</div>

				<div className="core-values-grid">
					{values.map((value, idx) => (
						<div 
							key={value.id}
							className="core-value-item"
							style={{
								opacity: visible ? 1 : 0,
								transform: visible ? 'translateY(0)' : 'translateY(40px)',
								transition: `all 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) ${idx * 0.1}s`,
							}}
						>
							<h3 className="core-value-title">{value.title}</h3>
							<p className="core-value-description">{value.description}</p>
						</div>
					))}
				</div>
			</div>
		</section>
	);
}
