#DefectIQ - Manufacturing Intelligence System

## Overview

DefectIQ  is a real-time manufacturing defect prediction and quality control monitoring system. The application enables operators to monitor sensor data, predict potential defects, and review historical predictions to improve manufacturing quality control.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Framework & Routing**
- React with TypeScript for type-safe component development
- Wouter for lightweight client-side routing
- Vite as the build tool and development server

**UI Component System**
- shadcn/ui component library (New York style variant) with Radix UI primitives
- Tailwind CSS for utility-first styling with CSS variables for theming
- Custom design system using Manrope font for UI and JetBrains Mono for data display
- Responsive design with mobile-first approach

**State Management**
- TanStack Query (React Query) for server state management and data fetching
- Query client configured with infinite stale time and disabled automatic refetching
- Local component state for UI interactions

**Data Visualization**
- Recharts library for rendering sensor data charts and analytics
- Real-time data visualization for temperature, pressure, vibration, and speed metrics

**Key Pages**
- Dashboard: Overview with real-time metrics and sensor monitoring
- Predict: Interactive form for analyzing manufacturing parameters and predicting defects
- History: Historical prediction records with filtering and statistics

### Backend Architecture

**Server Framework**
- Express.js HTTP server with TypeScript
- Custom logging middleware for request tracking
- Static file serving for production builds

**API Design**
- RESTful API endpoints under `/api` prefix
- JSON request/response format
- Zod schema validation for request payloads
- Standardized error handling with appropriate HTTP status codes

**Core Endpoints**
- `POST /api/predictions` - Create new defect predictions
- `GET /api/predictions` - Retrieve all predictions (ordered by timestamp)
- `GET /api/predictions/:id` - Get specific prediction by ID

**Data Layer**
- Storage abstraction layer (IStorage interface) for data operations
- DatabaseStorage implementation using Drizzle ORM
- Connection pooling for database efficiency

### Data Storage

**Database**
- PostgreSQL database via Neon serverless driver
- WebSocket support for real-time database connections
- Drizzle ORM for type-safe database queries and migrations

**Schema Design**
- `users` table: User authentication with UUID primary keys
- `predictions` table: Sensor data and defect predictions with fields:
  - Sensor readings: temperature, pressure, vibration, speed
  - Prediction results: probability (integer), risk level (Low/Medium/High)
  - Metadata: timestamp, operator, production line
  
**Type Safety**
- Drizzle-Zod integration for runtime validation
- Shared schema types between client and server
- Insert schemas for data validation

### Build & Deployment

**Development**
- Separate dev servers for client (Vite on port 5000) and server
- Hot Module Replacement (HMR) for rapid development
- Replit-specific plugins for enhanced development experience

**Production Build**
- esbuild for server bundling with selective dependency bundling
- Vite for optimized client bundle
- Single production server serving both API and static files
- Build artifacts output to `dist` directory

**Path Aliases**
- `@/` - Client source directory
- `@shared/` - Shared types and schemas
- `@assets/` - Static assets

### External Dependencies

**UI & Styling**
- Radix UI component primitives (dialogs, dropdowns, tooltips, etc.)
- Tailwind CSS with autoprefixer
- class-variance-authority for component variants
- lucide-react for iconography

**Data & Validation**
- Zod for schema validation
- date-fns for date manipulation
- React Hook Form with Zod resolvers for form handling

**Database**
- @neondatabase/serverless for PostgreSQL connection
- Drizzle ORM and Drizzle Kit for migrations
- ws package for WebSocket support

**Development Tools**
- TypeScript compiler with strict mode
- ESModule support throughout
- Replit-specific Vite plugins for enhanced development workflow
