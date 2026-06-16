import os
from PIL import Image

def find_pink_bottle():
    assets_dir = r"c:\Users\kavya\Desktop\Tirumala2\assets"
    src_path = os.path.join(assets_dir, "unique_5.jpg")
    
    if not os.path.exists(src_path):
        print(f"Source file not found: {src_path}")
        return
        
    img = Image.open(src_path).convert("RGB")
    width, height = img.size
    
    # We want to find the large pink bottle with handle.
    # In unique_5.jpg, there is a small pink bottle on the left, and a large pink bottle in the middle, and another large pink bottle further right, and a small pink bottle on the right.
    # Let's find all pink pixels:
    pink_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # Pink color: r high, g low, b medium-high
            if r > 180 and g < 100 and b > 110 and abs(r - b) < 60:
                pink_pixels.append((x, y))
                
    print(f"Found {len(pink_pixels)} pink pixels in unique_5.jpg.")
    
    # Let's cluster them or find the large pink bottle.
    # The large pink bottle with handle in the middle is approximately in the x-range [380, 480] or similar.
    # Let's group pink pixels by their x coordinate to see where they are clustered.
    x_hist = {}
    for x, y in pink_pixels:
        x_hist[x] = x_hist.get(x, 0) + 1
        
    # Print x coordinate clusters
    clusters = []
    current_cluster = []
    for x in sorted(x_hist.keys()):
        if not current_cluster or x - current_cluster[-1] <= 15:
            current_cluster.append(x)
        else:
            clusters.append(current_cluster)
            current_cluster = [x]
    if current_cluster:
        clusters.append(current_cluster)
        
    print(f"Found {len(clusters)} pink clusters:")
    for idx, c in enumerate(clusters):
        min_x, max_x = c[0], c[-1]
        pixel_count = sum(x_hist[x] for x in c)
        print(f"Cluster {idx}: x_range = [{min_x}, {max_x}], pixels = {pixel_count}")
        
        # Let's save a crop for each cluster to see what they are!
        cluster_pixels = [p for p in pink_pixels if min_x <= p[0] <= max_x]
        ys = [p[1] for p in cluster_pixels]
        min_y, max_y = min(ys), max(ys)
        
        # Add padding
        pad_x = 35
        pad_y = 50
        crop_box = (
            max(0, min_x - pad_x),
            max(0, min_y - pad_y),
            min(width, max_x + pad_x),
            min(height, max_y + pad_y)
        )
        
        cropped_img = img.crop(crop_box)
        crop_path = os.path.join(assets_dir, f"test_crop_pink_cluster_{idx}.png")
        cropped_img.save(crop_path)
        print(f"Saved cluster {idx} crop to {crop_path}")

if __name__ == '__main__':
    find_pink_bottle()
