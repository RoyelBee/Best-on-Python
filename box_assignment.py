from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
left, width = 0.0, .19
bottom, height = 0, 1
right = left + width
top = 1
fig = plt.figure(figsize=(12, 2))
ax = fig.add_axes([0, 0, 1, 1])  # Left, Bottom, Width, Height
# ---------- Remove border from the figures  ------------------
for item in [fig, ax]:
    item.patch.set_visible(False)
    fig.patch.set_visible(False)
    ax.axis('off')
# # -------------------------------------------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#00ffe1'
)
ax.add_patch(p)
kpi_label = 'MHK'
return_p = '125K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=34, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
# # # --- Box 2
left, width = .20, .19
bottom, height = .0, 1
right = left + width
top = 1
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#e100ff'
)
ax.add_patch(p)
kpi_label = 'FRD'
return_p = '80K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=34, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
# # -------- Box 3 ------------------------
left, width = .40, .19
bottom, height = .0, 1
right = left + width
top = 1
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#a7ff00'
)
ax.add_patch(p)
kpi_label = 'RNG'
return_p = '240K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
# # ----- Box 4 ---------------------------
left, width = .60, .19
bottom, height = .0, 1
right = left + width
top = 1
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#00a7ff'
)
ax.add_patch(p)
kpi_label = 'MOT'
return_p = '180K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
# # ----------- Box 5 --------
left, width = .80, .20
bottom, height = .0, 1
right = left + width
top = 1
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#ffe4c1'
)
ax.add_patch(p)
kpi_label = 'MIR'
return_p = '45K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
# plt.show()
plt.savefig('box.png')

img1 = Image.open('./box.png')
img2 = Image.open('./joined.png')
width, height = img1.size
imageSize = Image.new('RGB', (1200, 680))
imageSize.paste(img1, (0, 0))
imageSize.paste(img2, (0, height))
imageSize.save("box_bar.png")
print('Mail Send')
