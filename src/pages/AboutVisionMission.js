import React from 'react';
import VisionMission from '../components/About/visionMission';
import CoreValues from '../components/About/CoreValues';
import StrategicPriorities from '../components/About/StrategicPriorities';
import '../components/About/About.css';

export default function AboutVisionMission() {
  return (
    <main>
      <VisionMission />
      <CoreValues />
      <StrategicPriorities />
    </main>
  );
}
