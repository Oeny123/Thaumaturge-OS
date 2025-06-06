#!@GJS@ -m

const Gtk = imports.gi.Gtk;
const Gdk = imports.gi.Gdk;
//const { Gtk, Gdk } = imports.gi;

Gtk.init();
const monitors = Gdk.Display.get_default().get_monitors();
const details = [];
for (const m of monitors) {
    const { x, y, width, height } = m.get_geometry();
    details.push({ name: m.get_description(), x, y, width, height });
}

print(JSON.stringify(details));