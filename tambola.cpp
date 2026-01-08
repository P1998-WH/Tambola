#include <gtk/gtk.h>
#include <algorithm>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <vector>

struct AppState
{
    std::vector<int> remaining;
    std::mt19937 gen;
    GtkWidget* label;
};

static void update_label(AppState* state, const std::string& text)
{
    gtk_label_set_text(GTK_LABEL(state->label), text.c_str());
}

static void on_draw_number(GtkButton* /*button*/, gpointer data)
{
    auto* state = static_cast<AppState*>(data);
    if (state->remaining.empty())
    {
        update_label(state, "All numbers called");
        return;
    }

    std::uniform_int_distribution<size_t> dist(0, state->remaining.size() - 1);
    size_t index = dist(state->gen);
    int number = state->remaining[index];
    state->remaining.erase(state->remaining.begin() + static_cast<long>(index));

    std::ostringstream out;
    out << "Number: " << number << " (remaining: " << state->remaining.size() << ")";
    update_label(state, out.str());
}

int main(int argc, char** argv)
{
    gtk_init(&argc, &argv);

    AppState state;
    state.remaining.resize(90);
    std::iota(state.remaining.begin(), state.remaining.end(), 1);
    std::random_device rd;
    state.gen = std::mt19937(rd());

    GtkWidget* window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Tambola");
    gtk_window_set_default_size(GTK_WINDOW(window), 320, 180);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), nullptr);

    GtkWidget* box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 12);
    gtk_container_set_border_width(GTK_CONTAINER(box), 16);
    gtk_container_add(GTK_CONTAINER(window), box);

    state.label = gtk_label_new("Press Draw to start");
    gtk_box_pack_start(GTK_BOX(box), state.label, TRUE, TRUE, 0);

    GtkWidget* button = gtk_button_new_with_label("Draw");
    g_signal_connect(button, "clicked", G_CALLBACK(on_draw_number), &state);
    gtk_box_pack_start(GTK_BOX(box), button, FALSE, FALSE, 0);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}
