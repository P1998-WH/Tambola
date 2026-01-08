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
    GtkWidget* last_label;
    std::vector<GtkWidget*> number_boxes;
};

static void update_label(AppState* state, const std::string& text)
{
    gtk_label_set_text(GTK_LABEL(state->last_label), text.c_str());
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

    GtkWidget* box = state->number_boxes[static_cast<size_t>(number - 1)];
    GtkStyleContext* ctx = gtk_widget_get_style_context(box);
    gtk_style_context_add_class(ctx, "called");
}

static void on_reset(GtkButton* /*button*/, gpointer data)
{
    auto* state = static_cast<AppState*>(data);
    state->remaining.resize(90);
    std::iota(state->remaining.begin(), state->remaining.end(), 1);
    update_label(state, "Press Draw to start");

    for (GtkWidget* box : state->number_boxes)
    {
        GtkStyleContext* ctx = gtk_widget_get_style_context(box);
        gtk_style_context_remove_class(ctx, "called");
    }
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
    gtk_window_set_default_size(GTK_WINDOW(window), 520, 480);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), nullptr);

    GtkWidget* box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 12);
    gtk_container_set_border_width(GTK_CONTAINER(box), 16);
    gtk_container_add(GTK_CONTAINER(window), box);

    GtkCssProvider* css = gtk_css_provider_new();
    gtk_css_provider_load_from_data(
        css,
        ".num-box { background-color: #f2f2f2; border: 1px solid #000000; border-radius: 4px; }"
        ".called { background-color: #ffd24a; }"
        ".num-text { color: #1f1f1f; font-weight: 700; }",
        -1,
        nullptr);
    GdkScreen* screen = gdk_screen_get_default();
    gtk_style_context_add_provider_for_screen(
        screen, GTK_STYLE_PROVIDER(css), GTK_STYLE_PROVIDER_PRIORITY_USER);
    g_object_unref(css);

    state.last_label = gtk_label_new("Press Draw to start");
    gtk_box_pack_start(GTK_BOX(box), state.last_label, FALSE, FALSE, 0);

    GtkWidget* grid = gtk_grid_new();
    gtk_grid_set_row_spacing(GTK_GRID(grid), 6);
    gtk_grid_set_column_spacing(GTK_GRID(grid), 6);
    gtk_box_pack_start(GTK_BOX(box), grid, TRUE, TRUE, 0);

    state.number_boxes.resize(90);
    for (int i = 1; i <= 90; ++i)
    {
        std::ostringstream text;
        text << i;
        GtkWidget* label = gtk_label_new(text.str().c_str());
        GtkStyleContext* label_ctx = gtk_widget_get_style_context(label);
        gtk_style_context_add_class(label_ctx, "num-text");

        GtkWidget* event_box = gtk_event_box_new();
        GtkStyleContext* box_ctx = gtk_widget_get_style_context(event_box);
        gtk_style_context_add_class(box_ctx, "num-box");
        gtk_container_add(GTK_CONTAINER(event_box), label);
        gtk_widget_set_size_request(event_box, 36, 36);

        state.number_boxes[static_cast<size_t>(i - 1)] = event_box;
        int row = (i - 1) / 10;
        int col = (i - 1) % 10;
        gtk_grid_attach(GTK_GRID(grid), event_box, col, row, 1, 1);
    }

    GtkWidget* controls = gtk_box_new(GTK_ORIENTATION_HORIZONTAL, 12);
    gtk_box_pack_start(GTK_BOX(box), controls, FALSE, FALSE, 0);

    GtkWidget* draw_button = gtk_button_new_with_label("Draw");
    g_signal_connect(draw_button, "clicked", G_CALLBACK(on_draw_number), &state);
    gtk_box_pack_start(GTK_BOX(controls), draw_button, TRUE, TRUE, 0);

    GtkWidget* reset_button = gtk_button_new_with_label("Reset");
    g_signal_connect(reset_button, "clicked", G_CALLBACK(on_reset), &state);
    gtk_box_pack_start(GTK_BOX(controls), reset_button, TRUE, TRUE, 0);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}
