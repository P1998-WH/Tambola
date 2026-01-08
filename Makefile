APP := tambola
SRC := tambola.cpp

CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -O2
GTK_CFLAGS := $(shell pkg-config --cflags gtk+-3.0)
GTK_LIBS := $(shell pkg-config --libs gtk+-3.0)

all: $(APP)

$(APP): $(SRC)
	$(CXX) $(CXXFLAGS) $(GTK_CFLAGS) -o $@ $^ $(GTK_LIBS)

run: $(APP)
	./$(APP)

clean:
	rm -f $(APP)

.PHONY: all run clean
