# Graphics library (libgraph)

`libgraph` provides a queued 2D drawing API for framebuffer-backed graphics adapters such as `virtio-gpu`, `vga`, and
`cirrus`.

The public interface is declared in `<graph.h>`. Applications initialize the library, open a `graph_t` context for an
adapter, set a mode, queue drawing operations, and close the context before shutting the library down.

## Adapters and queues

| Constant | Meaning |
| --- | --- |
| `GRAPH_NONE` | No adapter. Passing it to `graph_open()` fails with `-ENODEV`. |
| `GRAPH_VIRTIOGPU` | Generic VirtIO GPU adapter. |
| `GRAPH_VGA` | Generic VGA adapter. |
| `GRAPH_CIRRUS` | Cirrus Logic adapter. |
| `GRAPH_ANY` | Select the first available adapter in implementation order. |

| Queue | Use |
| --- | --- |
| `GRAPH_QUEUE_HIGH` | High-priority task queue. |
| `GRAPH_QUEUE_LOW` | Low-priority task queue. |
| `GRAPH_QUEUE_DEFAULT` | Alias for `GRAPH_QUEUE_LOW`. |
| `GRAPH_QUEUE_BOTH` | Accepted by queue-control functions such as `graph_stop()` and `graph_reset()`. |

Drawing functions accept `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
They return `-EINVAL` for other queue values.

## Data structures

`graph_t`
: Graphics context opened by `graph_open()`. It stores framebuffer dimensions, color depth, task queues, a mutex, and
  adapter function pointers.

`graph_font_t`
: Font descriptor used by `graph_print()`. It stores glyph width, glyph height, row span, first character offset, and
  bitmap data pointer.

`graph_mode_t`
: Display mode selector. The enum includes power-management modes, 8-bit indexed modes, 16-bit `5:6:5` modes, 24-bit
  modes, and 32-bit modes.

`graph_freq_t`
: Refresh-rate selector. The enum includes `GRAPH_DEFFREQ`, `GRAPH_24Hz`, `GRAPH_60Hz`, `GRAPH_120Hz`, and other
  fixed rates declared in `<graph.h>`.

`graph_fill_t`
: Polygon fill algorithm. `GRAPH_FILL_FLOOD` selects flood fill, and `GRAPH_FILL_BOUND` selects boundary fill.

## Lifecycle functions

````{function} graph_init()
Initializes the adapter backends linked into the image.

The function initializes `cirrus`, `virtio-gpu`, and `vga` backends in that order.

:returns: `EOK` on success or the first negative error returned by a backend initializer.
````

````{function} graph_done()
Destroys global adapter backend state.

:returns: Nothing.
````

````{function} graph_open(graph, adapter, mem)
Opens a graphics context and allocates high- and low-priority task queues.

The queue memory is split equally between high and low queues. The function sets software drawing handlers first and
then opens the selected hardware adapter.

:param graph: Uninitialized graphics context supplied by the caller.
:param adapter: Adapter mask or `GRAPH_ANY`.
:param mem: Total task queue memory in bytes.
:returns: `EOK` on success, `-EINVAL` when `mem` is too small for two tasks and a wrap marker, `-ENOMEM` on queue
  allocation failure, `-ENODEV` when no selected adapter opens, or a negative mutex or adapter error.
````

````{function} graph_close(graph)
Closes the adapter context, destroys the context mutex, and frees task queue memory.

:param graph: Graphics context opened by `graph_open()`.
:returns: Nothing.
````

````{function} graph_mode(graph, mode, freq)
Resets both task queues, waits until the adapter is idle, and sets the selected display mode.

:param graph: Graphics context opened by `graph_open()`.
:param mode: Display mode from `graph_mode_t`.
:param freq: Refresh-rate selector from `graph_freq_t`.
:returns: Adapter-specific result from the context `mode` handler.
````

## Drawing functions

````{function} graph_line(graph, x, y, dx, dy, stroke, color, queue)
Draws a line task or queues it when the adapter is busy.

:param graph: Graphics context opened by `graph_open()`.
:param x: Start point x coordinate in pixels.
:param y: Start point y coordinate in pixels.
:param dx: Horizontal delta in pixels.
:param dy: Vertical delta in pixels.
:param stroke: Line thickness in pixels.
:param color: Adapter color value.
:param queue: `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
:returns: `EOK`, `-EINVAL`, `-EACCES`, `-ENOSPC`, or an adapter drawing error.
````

````{function} graph_rect(graph, x, y, dx, dy, color, queue)
Draws a filled rectangle task or queues it when the adapter is busy.

:param graph: Graphics context opened by `graph_open()`.
:param x: Rectangle x coordinate in pixels.
:param y: Rectangle y coordinate in pixels.
:param dx: Rectangle width in pixels.
:param dy: Rectangle height in pixels.
:param color: Adapter color value.
:param queue: `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
:returns: `EOK`, `-EINVAL`, `-EACCES`, `-ENOSPC`, or an adapter drawing error.
````

````{function} graph_fill(graph, x, y, color, type, queue)
Fills a region starting at `(x, y)` with the selected fill algorithm.

:param graph: Graphics context opened by `graph_open()`.
:param x: Seed point x coordinate in pixels.
:param y: Seed point y coordinate in pixels.
:param color: Adapter color value.
:param type: `GRAPH_FILL_FLOOD` or `GRAPH_FILL_BOUND`.
:param queue: `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
:returns: `EOK`, `-EINVAL`, `-EACCES`, `-ENOSPC`, or an adapter drawing error.
````

````{function} graph_print(graph, font, text, x, y, dx, dy, color, queue)
Draws text by queueing one glyph task per character.

The glyph bitmap address is computed from `font->data`, `font->height`, `font->span`, `font->offs`, and the current
character value.

:param graph: Graphics context opened by `graph_open()`.
:param font: Font descriptor.
:param text: Null-terminated text string.
:param x: First glyph x coordinate in pixels.
:param y: First glyph y coordinate in pixels.
:param dx: Requested glyph width. The implementation scales it by `font->width / font->height`.
:param dy: Glyph height passed to the adapter.
:param color: Adapter color value.
:param queue: `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
:returns: `EOK` after all glyphs are queued or drawn, or the first negative result from the task queue path.
````

````{function} graph_move(graph, x, y, dx, dy, mx, my, queue)
Moves a rectangular framebuffer region by `(mx, my)` pixels.

:param graph: Graphics context opened by `graph_open()`.
:param x: Source x coordinate in pixels.
:param y: Source y coordinate in pixels.
:param dx: Region width in pixels.
:param dy: Region height in pixels.
:param mx: Horizontal move delta in pixels.
:param my: Vertical move delta in pixels.
:param queue: `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
:returns: `EOK`, `-EINVAL`, `-EACCES`, `-ENOSPC`, or an adapter drawing error.
````

````{function} graph_copy(graph, src, dst, dx, dy, srcspan, dstspan, queue)
Copies a rectangular bitmap region from `src` to `dst`.

:param graph: Graphics context opened by `graph_open()`.
:param src: Source bitmap pointer.
:param dst: Destination bitmap or framebuffer pointer.
:param dx: Region width in pixels.
:param dy: Region height in pixels.
:param srcspan: Source row span in bytes.
:param dstspan: Destination row span in bytes.
:param queue: `GRAPH_QUEUE_HIGH`, `GRAPH_QUEUE_LOW`, or `GRAPH_QUEUE_DEFAULT`.
:returns: `EOK`, `-EINVAL`, `-EACCES`, `-ENOSPC`, or an adapter drawing error.
````

## Color and cursor functions

````{function} graph_colorset(graph, colors, first, last)
Sets adapter palette entries in an indexed-color mode.

:param graph: Graphics context opened by `graph_open()`.
:param colors: Color map data.
:param first: First palette index to set.
:param last: Last palette index to set.
:returns: Adapter-specific result from the context `colorset` handler.
````

````{function} graph_colorget(graph, colors, first, last)
Reads adapter palette entries in an indexed-color mode.

:param graph: Graphics context opened by `graph_open()`.
:param colors: Output color map buffer.
:param first: First palette index to read.
:param last: Last palette index to read.
:returns: Adapter-specific result from the context `colorget` handler.
````

````{function} graph_cursorset(graph, amask, xmask, bg, fg)
Sets the hardware cursor masks and colors.

:param graph: Graphics context opened by `graph_open()`.
:param amask: AND mask data.
:param xmask: XOR mask data.
:param bg: Background color value.
:param fg: Foreground color value.
:returns: Adapter-specific result from the context `cursorset` handler.
````

````{function} graph_cursorpos(graph, x, y)
Updates the cursor position.

:param graph: Graphics context opened by `graph_open()`.
:param x: Cursor x coordinate in pixels.
:param y: Cursor y coordinate in pixels.
:returns: Adapter-specific result from the context `cursorpos` handler.
````

````{function} graph_cursorshow(graph)
Shows the cursor.

:param graph: Graphics context opened by `graph_open()`.
:returns: Adapter-specific result from the context `cursorshow` handler.
````

````{function} graph_cursorhide(graph)
Hides the cursor.

:param graph: Graphics context opened by `graph_open()`.
:returns: Adapter-specific result from the context `cursorhide` handler.
````

## Queue and synchronization functions

````{function} graph_commit(graph)
Flushes framebuffer changes through the adapter commit handler.

:param graph: Graphics context opened by `graph_open()`.
:returns: Adapter-specific result from the context `commit` handler.
````

````{function} graph_trigger(graph)
Triggers adapter execution of the next queued task.

:param graph: Graphics context opened by `graph_open()`.
:returns: Adapter-specific result from the context `trigger` handler.
````

````{function} graph_stop(graph, queue)
Disables accepting new tasks on selected queues.

For `GRAPH_QUEUE_BOTH`, both queues are stopped. For `GRAPH_QUEUE_HIGH` or `GRAPH_QUEUE_LOW`, only that queue is
stopped.

:param graph: Graphics context opened by `graph_open()`.
:param queue: Queue selector.
:returns: `EOK`.
````

````{function} graph_start(graph, queue)
Decrements the stop counter on selected queues and re-enables queueing when the counter reaches `0`.

:param graph: Graphics context opened by `graph_open()`.
:param queue: Queue selector.
:returns: `EOK`.
````

````{function} graph_tasks(graph, queue)
Returns the number of tasks waiting in selected queues.

For `GRAPH_QUEUE_BOTH`, the function returns the sum of high- and low-priority tasks.

:param graph: Graphics context opened by `graph_open()`.
:param queue: Queue selector.
:returns: Number of queued tasks.
````

````{function} graph_reset(graph, queue)
Clears selected queues and resets their stop counters.

:param graph: Graphics context opened by `graph_open()`.
:param queue: Queue selector.
:returns: `EOK`.
````

````{function} graph_vsync(graph)
Returns the number of vertical synchronizations since the previous adapter `vsync` call.

:param graph: Graphics context opened by `graph_open()`.
:returns: Adapter-specific result from the context `vsync` handler.
````

## Minimal use

```c
#include <graph.h>

int main(void)
{
    graph_t graph;

    if (graph_init() < 0)
        return 1;

    if (graph_open(&graph, GRAPH_ANY, 0x2000) < 0)
        return 1;

    graph_mode(&graph, GRAPH_DEFMODE, GRAPH_DEFFREQ);
    graph_rect(&graph, 0, 0, graph.width, graph.height, 0x000000, GRAPH_QUEUE_HIGH);
    graph_line(&graph, 0, 0, graph.width, graph.height, 1, 0xffffff, GRAPH_QUEUE_HIGH);
    graph_commit(&graph);

    graph_close(&graph);
    graph_done();
    return 0;
}
```

Example applications that use `libgraph` are available in `_user/rotrectangle` and `_user/voxeldemo`.