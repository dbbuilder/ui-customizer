# UI Customizer Tool

A comprehensive tool that generates dynamic, customizable UI components for Vue.js and React applications using Tailwind CSS. Designed to eliminate cookie-cutter appearances and provide extensive customization options through algorithmic design generation.

## 🌟 Features

### Design Generation Engine
- **Unique Design Variations**: Generate distinctive designs using advanced color theory and typography principles
- **Multiple Design Styles**: Support for modern, minimalist, brutalist, glassmorphism, neumorphism, retro, organic, and geometric styles
- **Intelligent Color Palettes**: Generate accessible color schemes with WCAG 2.1 AA compliance
- **Smart Typography Pairing**: Automatic font pairing with optimal scale ratios and line heights
- **Consistent Spacing Systems**: Mathematical spacing scales for perfect visual rhythm

### Component Library Generation
- **20+ Component Types**: Buttons, forms, cards, navigation, modals, tables, layouts, and more
- **Framework Support**: Generate components for both Vue.js 3 and React with TypeScript support
- **Accessibility Built-in**: ARIA labels, keyboard navigation, and screen reader compatibility
- **Responsive Design**: Mobile-first responsive implementations with custom breakpoints
- **State Management**: Interactive components with proper state handling

### Real-time Preview System
- **Live Updates**: Instant preview updates as you modify design parameters
- **Multi-viewport Testing**: Preview components across mobile, tablet, desktop, and wide screen sizes
- **Interactive States**: Test hover, focus, active, and disabled component states
- **Code Export**: Export production-ready code with complete documentation
- **Screenshot Generation**: Generate component previews for design documentation

### Advanced Customization
- **Visual Controls**: Intuitive color pickers with palette generation
- **Typography Management**: Font selection, pairing, and scale customization
- **Layout Controls**: Spacing, sizing, and positioning adjustments
- **Animation System**: Timing, easing, and transition customization
- **Preset Management**: Save, load, and share custom design configurations

## 🛠️ Technology Stack

### Frontend
- **Vue.js 3** with Composition API and TypeScript
- **Tailwind CSS** for utility-first styling
- **Vite** for fast development and building
- **Pinia** for state management
- **Headless UI** for accessible base components
- **Prism.js** for syntax highlighting
- **File-saver & JSZip** for code export functionality

### Backend
- **FastAPI** (Python 3.9+) for high-performance API
- **Jinja2** for code template generation
- **Colour & Colorsys** for advanced color processing
- **Pydantic** for data validation and serialization
- **Uvicorn** for ASGI server
- **Python-multipart** for file uploads

### Development Tools
- **TypeScript** for type safety
- **ESLint & Prettier** for code quality
- **Vitest** for unit testing
- **Cypress** for end-to-end testing
- **pytest** for backend testing

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm/yarn
- Python 3.9+
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/dbbuilder/ui-customizer.git
cd ui-customizer
```

2. **Set up the backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

3. **Set up the frontend**
```bash
cd frontend
npm install
npm run dev
```

4. **Access the application**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/api/docs

## 📖 Usage

### Basic Usage

1. **Select Design Style**: Choose from modern, minimalist, brutalist, or other design styles
2. **Configure Colors**: Use the color picker or enter hex values for your base palette
3. **Customize Typography**: Select font families and adjust scale ratios
4. **Adjust Spacing**: Modify the spacing system to match your design needs
5. **Preview Components**: View real-time updates across different viewport sizes
6. **Export Code**: Download production-ready Vue.js or React components

## 📁 Project Structure

```
ui-customizer/
├── frontend/                 # Vue.js frontend application
│   ├── src/
│   │   ├── components/       # Vue components
│   │   ├── stores/           # Pinia stores
│   │   ├── types/            # TypeScript definitions
│   │   └── utils/            # Utility functions
│   └── package.json          # Frontend dependencies
├── backend/                  # FastAPI backend application
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   ├── services/         # Business logic
│   │   └── utils/            # Utility functions
│   └── requirements.txt      # Python dependencies
└── README.md                 # Project documentation
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [Vue.js](https://vuejs.org/) for the reactive frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) for the high-performance Python API framework

---

Made with ❤️ by the UI Customizer Tool team