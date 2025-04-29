
CREATE TABLE IF NOT EXISTS campaigns (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT CHECK (status IN ('Active', 'Paused')) NOT NULL,
    clicks INTEGER NOT NULL,
    cost NUMERIC(10, 2) NOT NULL,
    impressions INTEGER NOT NULL
);


INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale', 'Active', 150, 45.99, 1000),
('Black Friday', 'Paused', 320, 89.50, 2500),
('Spring Promo', 'Active', 200, 60.25, 1800),
('Holiday Deals', 'Paused', 90, 20.00, 800),
('Flash Sale', 'Active', 450, 130.75, 3000),
('Clearance Event', 'Paused', 110, 35.10, 1200),
('Winter Campaign', 'Active', 260, 78.00, 2100),
('Back to School', 'Paused', 175, 50.99, 1400),
('Weekend Blast', 'Active', 330, 99.90, 2700),
('Mega Discount', 'Paused', 80, 15.75, 600);
