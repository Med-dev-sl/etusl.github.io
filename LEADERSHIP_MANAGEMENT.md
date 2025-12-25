# Leadership Management System

This document describes the leadership and principal officers management system for the university website.

## Backend Setup

### Models

#### LeaderPosition
Defines leadership position titles with hierarchical levels.

**Fields:**
- `title` (CharField, max_length=200): Position title (e.g., "Chancellor", "Registrar")
- `hierarchy_level` (IntegerField, choices 1-3): 
  - Level 1: Top leadership (Chancellor, Vice-Chancellor)
  - Level 2: Middle management (Chairperson, Pro-Vice-Chancellor)
  - Level 3: Directorate and lower positions (Registrar, Bursar, Directors)
- `order` (IntegerField): Display order within the same hierarchy level
- `created_at` (DateTimeField, auto_now_add=True)
- `updated_at` (DateTimeField, auto_now=True)

**Meta:**
- Ordering: `('hierarchy_level', 'order')`

#### Leader
Individual leader profile with authentication binding.

**Fields:**
- `user` (OneToOneField to User): Links to Django user for authentication and permission control
- `position` (ForeignKey to LeaderPosition): The leader's position
- `name` (CharField, max_length=200): Full name
- `photo` (ImageField, optional): Leader's photo
- `bio` (TextField, optional): Biography and background
- `email` (EmailField): Contact email
- `phone` (CharField, optional): Contact phone number
- `order` (IntegerField): Display order
- `created_at` (DateTimeField, auto_now_add=True)
- `updated_at` (DateTimeField, auto_now=True)

**Meta:**
- Ordering: `('position__hierarchy_level', 'order', 'name')`

### API Endpoints

#### GET /api/leader-positions/
List all leadership positions.

**Query Parameters:**
- `ordering`: Sort by specified field (e.g., `?ordering=hierarchy_level,order`)

**Response:**
```json
{
  "count": 6,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Chancellor",
      "hierarchy_level": 1,
      "order": 1,
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```

#### GET /api/leaders/
List all leaders with hierarchical ordering.

**Query Parameters:**
- `ordering`: Sort by specified field (default: `position__hierarchy_level,order`)
- `position`: Filter by position ID

**Response:**
```json
{
  "count": 6,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": 1,
      "position": 1,
      "position_title": "Chancellor",
      "position_level": 1,
      "name": "Prof. Chancellor",
      "photo": "http://example.com/media/leaders/photo.jpg",
      "bio": "Biography text...",
      "email": "chancellor@university.edu",
      "phone": "+1-234-567-8900",
      "order": 1,
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```

#### GET /api/leaders/{id}/
Retrieve a specific leader's profile.

#### PATCH /api/leaders/{id}/
Update a leader's profile (leaders can only update their own profile).

**Permission:** `IsOwnerOrReadOnly`
- Leaders can only PATCH their own profile (identified by `user` field)
- Superusers and staff can PATCH any profile
- All users can GET/list leaders

**Request Body:**
```json
{
  "name": "Prof. Updated Name",
  "bio": "Updated biography...",
  "email": "new.email@university.edu",
  "phone": "+1-234-567-8901"
}
```

**Note:** `user`, `position`, and `order` fields cannot be modified via API (admin only).

### Admin Interface

#### LeaderPosition Admin
- List Display: Title, Hierarchy Level, Order, Created Date
- Ordering: Hierarchy Level, Order
- Read-only: Created At, Updated At

#### Leader Admin
- List Display: Name, Position, Order, Photo Preview, User, Created Date
- Filtering: By hierarchy level, position
- Search: By name, bio, email
- Read-only: Photo Preview, Created At, Updated At
- Fieldsets: Personal Information, Position, Biography & Contact, Display, Timestamps

**Staff User Access:**
- Non-superuser staff can only view and edit their own profile in the admin interface
- Superusers can view and edit all leaders

## Frontend Setup

### Components

#### PrincipalOfficers
React component that displays leaders in a hierarchical grid layout with animations.

**Location:** `src/components/About/PrincipalOfficers.js`

**Features:**
- Fetches leader data from `/api/leaders/`
- Groups leaders by hierarchy level (1, 2, 3)
- Displays with staggered slide-up animations using Intersection Observer
- Shows placeholder images with initials if no photo is provided
- Responsive design (supports mobile, tablet, desktop)

**Usage:**
```jsx
import PrincipalOfficers from './components/About/PrincipalOfficers';

export default function LeadershipPage() {
  return <PrincipalOfficers />;
}
```

#### LeadershipDirectorates
Container component that integrates PrincipalOfficers into the leadership page.

**Location:** `src/components/About/leadershipDirectorates.js`

**Usage in Page:**
```jsx
import Leadership from '../components/About/leadershipDirectorates';

export default function AboutLeadership() {
  return (
    <>
      <HeroSection />
      <Leadership />
      <Footer />
    </>
  );
}
```

### Styling

**CSS File:** `src/components/About/About.css`

**Key Classes:**
- `.principal-officers-section`: Main section wrapper with gradient background
- `.officers-grid`: Container for hierarchical layout
- `.officers-level-1`, `.officers-level-2`, `.officers-level-3`: Level-specific grid layouts
- `.officer-card`: Individual card with animation
- `.officer-photo`: Circular profile photo with gold border
- `.officer-name`: Leader's name heading
- `.officer-title`: Position title in gold color
- `.officer-bio`: Biography text

**Animations:**
- Slide-up animation with staggered delays
- Uses cubic-bezier(0.34, 1.56, 0.64, 1) for smooth easing
- Triggered on scroll with Intersection Observer

**Responsive Breakpoints:**
- Desktop (1200px+): 1-1-2 hierarchical grid layout
- Tablet (980px-1200px): Adjusted spacing and sizing
- Mobile (768px): Full-width cards
- Small Mobile (480px): Minimal padding and sizing

## Setup Instructions

### 1. Database Migration
```bash
cd backend
python manage.py migrate api
```

### 2. Populate Sample Data
```bash
python manage.py populate_leaders
```

This creates:
- 6 leadership positions with proper hierarchy levels
- 6 sample leaders linked to user accounts
- Users with read/write permissions mapped to their profiles

### 3. Create Additional Leaders (Admin)

1. Go to Django admin (`/admin/`)
2. Navigate to "Leader Positions" section
3. Create new positions as needed with hierarchy levels
4. Navigate to "Leaders" section
5. Create new leaders and link them to user accounts

### 4. Access in Frontend

The leadership page is accessible at `/about/leadership` route, displaying all leaders in hierarchical order with photos and animations.

## Permission Model

### Authentication Levels

1. **Anonymous User**: Can view all leaders (GET only)
2. **Authenticated User (Leader)**: Can view all leaders and edit only their own profile
3. **Staff User**: Can view and edit all profiles (if superuser)
4. **Superuser**: Full access to all operations

### API Permission Check

The `IsOwnerOrReadOnly` custom permission class enforces:
- SAFE_METHODS (GET, HEAD, OPTIONS): Allowed for all users
- Unsafe methods (POST, PUT, PATCH, DELETE): 
  - Allowed if `request.user == obj.user` (owner)
  - Allowed if `request.user.is_staff` (superuser/staff)

### Example: Leader Updating Own Profile

```javascript
// Frontend: Authenticated as leader with ID 1
const updateProfile = async (leaderId, updates) => {
  try {
    const response = await axios.patch(
      `/api/leaders/${leaderId}/`,
      updates,
      {
        headers: {
          'Authorization': `Bearer ${authToken}`
        }
      }
    );
    return response.data;
  } catch (error) {
    if (error.response?.status === 403) {
      console.error('Permission denied: Leaders can only edit their own profile');
    }
  }
};

// Only leader with ID 1 (user linked to this leader) can update
updateProfile(1, { bio: 'New bio...', phone: '+1-234-567-8901' });
```

## File Structure

```
backend/
├── api/
│   ├── models.py              # LeaderPosition, Leader models
│   ├── serializers.py         # LeaderPositionSerializer, LeaderSerializer
│   ├── views.py               # LeaderViewSet, custom IsOwnerOrReadOnly permission
│   ├── urls.py                # API route registration
│   ├── admin.py               # LeaderPositionAdmin, LeaderAdmin
│   └── management/
│       └── commands/
│           └── populate_leaders.py  # Sample data population

src/
├── pages/
│   └── AboutLeadership.js      # Leadership page with hero section
├── components/About/
│   ├── PrincipalOfficers.js    # Leader grid component
│   ├── leadershipDirectorates.js  # Container component
│   └── About.css               # All styling including animations
```

## Testing the System

### 1. View Leaders
```bash
curl http://localhost:8000/api/leaders/
```

### 2. Test Permission Control
```bash
# Try to update another leader's profile (should fail)
curl -X PATCH http://localhost:8000/api/leaders/2/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"bio":"Hacked!"}'

# Response: 403 Forbidden
```

### 3. Update Own Profile (should succeed)
```bash
# Logged in as leader with ID 1
curl -X PATCH http://localhost:8000/api/leaders/1/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"bio":"Updated biography","phone":"+1-987-654-3210"}'

# Response: 200 OK with updated data
```

## Future Enhancements

1. **Photo Upload UI**: Add frontend form for leaders to upload/change their photo
2. **Directorate Subsection**: Group level 3 leaders by department
3. **Contact Form Integration**: Allow students/staff to contact leaders
4. **Search/Filter**: Add frontend search for leaders
5. **Audit Trail**: Track changes to leader profiles
6. **Notification System**: Alert leaders when their profile is viewed/contacted
