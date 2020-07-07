#
import matplotlib.pyplot as plt
import matplotlib.patches as patches

left, width = 0.0, .48
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
    color='#fcea17'
)
ax.add_patch(p)

kpi_label = 'Return'
return_p = '1.2%'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# # # --- Box 2
left, width = .50, .50
bottom, height = .0, 1
right = left + width
top = 1
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#25f4b5'
)
ax.add_patch(p)

kpi_label = 'MTD'
return_p = '.82%'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5 * (left + right), .3 * (bottom + top), return_p,
        ha='center',
        va='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
#
# plt.show()
plt.savefig('box.png')
