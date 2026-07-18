const sharp = require('sharp');
const fs = require('fs');
const png2icons = require('png2icons');
const path = require('path');

const svgPath = path.join(__dirname, 'src', 'icons', 'icon.svg');
const outDir = path.join(__dirname, 'src-tauri', 'icons');

async function generate() {
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

    const svg = fs.readFileSync(svgPath);

    // Generate PNGs
    await sharp(svg).resize(32, 32).png().toFile(path.join(outDir, '32x32.png'));
    await sharp(svg).resize(128, 128).png().toFile(path.join(outDir, '128x128.png'));
    await sharp(svg).resize(256, 256).png().toFile(path.join(outDir, 'icon.png'));

    // Generate ICO from 256px PNG
    const png256 = fs.readFileSync(path.join(outDir, 'icon.png'));
    const ico = png2icons.createICO(png256, png2icons.BILINEAR, 0, true, true);
    if (ico) fs.writeFileSync(path.join(outDir, 'icon.ico'), ico);

    console.log('Icons generated in src-tauri/icons/');
}

generate().catch(console.error);
