# 🍽️ FoodHub - Food Ordering E-commerce Website

A modern, responsive food ordering website built using **only HTML5 and CSS3** (no JavaScript!). This project demonstrates advanced CSS techniques including Flexbox, CSS Grid, and the checkbox hack for interactive cart functionality.

## 📋 Project Overview

This is a Swiggy/Zomato-inspired food delivery website that showcases:
- Clean, modern UI design
- Fully responsive layout (mobile, tablet, desktop)
- Interactive cart system using pure CSS
- Smooth animations and hover effects
- Professional food e-commerce interface

## ✨ Features

### 🎨 Design Features
- **Responsive Layout**: Works seamlessly on mobile, tablet, and desktop devices
- **Modern UI**: Clean, professional design with Swiggy/Zomato-inspired aesthetics
- **CSS Grid**: Food items displayed in a responsive grid layout
- **Flexbox**: Header, navigation, and cart use flexible layouts
- **Custom Color Scheme**: Professional color palette with CSS variables

### 🛒 Cart Functionality (CSS Only!)
- **Add to Cart**: Click "Add to Cart" to add items (using checkbox hack)
- **Visual Feedback**: Button changes to green with checkmark when item is added
- **Cart Sidebar**: Slide-out cart panel showing all added items
- **Remove Items**: Click "Remove" to take items out of cart
- **Cart Badge**: Shows cart item count (visual indicator)
- **No JavaScript**: All functionality implemented with CSS `:checked` selector

### 🍕 Food Card Components
- Food image with hover zoom effect
- Food name and description
- Star ratings (★★★★☆)
- Delivery time display (⏱️)
- Veg/Non-Veg indicators (🟢/🔴)
- Offer badges (20% OFF, etc.)
- Price display
- Interactive "Add to Cart" button

### 🎭 Animations & Effects
- **Hover Effects**: Cards lift on hover with shadow
- **Image Zoom**: Food images scale on hover
- **Button Animations**: Smooth color transitions and scale effects
- **Cart Slide**: Smooth sidebar animation
- **Loading Effect**: Shimmer effect on images
- **Shine Effect**: Light sweep on card hover
- **Pulse Animation**: Button feedback on click

### 📱 Responsive Breakpoints
- **Desktop**: Full layout with all features (>768px)
- **Tablet**: Adjusted grid and navigation (768px)
- **Mobile**: Single column layout, fixed cart button (<480px)

## 📁 Project Structure

```
E-commerce (Food E-commerce)/
├── index.html          # Main HTML file with all sections
├── style.css           # Complete CSS styling and animations
├── images/             # Folder for food images (using web URLs currently)
└── README.md           # This file
```

## 🚀 How to Run

1. **Download/Clone** the project folder
2. **Open** `index.html` in any modern web browser
3. **Interact** with the website:
   - Click categories to explore
   - Click "Add to Cart" on food items
   - Click the "🛒 Cart" button to view cart sidebar
   - Click "Remove" to remove items from cart

## 🎯 Key Sections

### 1. Header
- Logo: FoodHub branding
- Search Bar: Search for food items
- Navigation: Home, Categories, Offers, Help
- Cart Button: Opens cart sidebar

### 2. Hero Banner
- Eye-catching gradient background
- Tagline and call-to-action message

### 3. Categories Section
- 8 food categories with emoji icons
- Hover effects on category cards
- Responsive grid layout

### 4. Food Listing
- 9 food items with complete details
- Each card includes:
  - High-quality food image
  - Food name and description
  - Star rating (visual only)
  - Delivery time
  - Veg/Non-Veg badge
  - Offer badge (where applicable)
  - Price
  - Add to Cart button

### 5. Cart Sidebar
- Slides in from right when cart button clicked
- Shows all added items
- Item name and price for each
- Remove button for each item
- Total price display (visual only)
- Checkout button

### 6. Footer
- Company information
- Quick links
- Copyright notice

## 🔧 CSS Techniques Used

### Layout
- **CSS Grid**: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`
- **Flexbox**: `display: flex; justify-content: space-between`
- **Sticky Header**: `position: sticky; top: 0`
- **Fixed Elements**: Cart button on mobile

### Interactive Features (No JavaScript!)
- **Checkbox Hack**: `input:checked ~ .element`
- **CSS Selectors**: `:hover`, `:focus-within`, `:checked`, `:active`
- **Sibling Selectors**: `~` and `+`
- **Pseudo-elements**: `::before`, `::after`

### Animations
```css
@keyframes slideInCart {
    from { opacity: 0; transform: translateX(20px); }
    to { opacity: 1; transform: translateX(0); }
}
```

### Responsive Design
```css
@media (max-width: 768px) { /* Tablet styles */ }
@media (max-width: 480px) { /* Mobile styles */ }
```

## 🎨 Color Palette

- **Primary**: `#fc8019` (Orange - Swiggy-inspired)
- **Secondary**: `#60b246` (Green - Success)
- **Danger**: `#e23744` (Red - Offers/Non-Veg)
- **Dark Text**: `#282c3f`
- **Light Text**: `#686b78`
- **Background**: `#f9f9f9`

## 📦 Food Items Included

1. **Margherita Pizza** - ₹299 (Veg, 20% OFF)
2. **Chicken Burger** - ₹199 (Non-Veg)
3. **Hyderabadi Biryani** - ₹349 (Non-Veg, 15% OFF)
4. **Chocolate Cake** - ₹149 (Veg)
5. **Veg Hakka Noodles** - ₹179 (Veg)
6. **Paneer Tikka** - ₹249 (Veg, 25% OFF)
7. **Mexican Tacos** - ₹229 (Non-Veg)
8. **BBQ Chicken Wings** - ₹279 (Non-Veg, 30% OFF)
9. **Caesar Salad** - ₹199 (Veg)

## 🌐 Browser Compatibility

- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Opera

## 📝 Learning Outcomes

This project demonstrates:
- Advanced CSS layout techniques (Grid + Flexbox)
- Pure CSS interactivity without JavaScript
- Responsive web design principles
- Modern UI/UX patterns
- CSS animations and transitions
- Professional code organization
- CSS custom properties (variables)

## 🚫 Limitations (By Design)

Since this is a **CSS-only** project:
- Cart count doesn't calculate dynamically
- Total price is static
- No actual checkout functionality
- Search bar is visual only
- No real data persistence

These limitations are **intentional** to showcase what's possible with HTML/CSS alone!

## 🎓 Beginner-Friendly

All code is:
- ✅ Well-commented
- ✅ Properly formatted
- ✅ Using clear naming conventions
- ✅ Organized in logical sections
- ✅ Following best practices

## 🔮 Future Enhancements (Would Require JavaScript)

- Dynamic cart total calculation
- Local storage for cart persistence
- Filter/sort functionality
- Search implementation
- Form validation
- Dynamic content loading

## 📧 Credits

- **Food Images**: Unsplash (royalty-free)
- **Design Inspiration**: Swiggy, Zomato
- **Icons**: Unicode Emojis
- **Fonts**: System fonts (Segoe UI)

## 📄 License

This is a learning project - feel free to use and modify for educational purposes!

---

**Built with ❤️ using only HTML5 & CSS3**

*No JavaScript. No Frameworks. Just Pure CSS Magic!* ✨
