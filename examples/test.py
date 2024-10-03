import polars as pl
from great_tables import GT, md, html
from great_tables.data import islands

islands_mini = (
    pl.from_pandas(islands).sort("size", descending=True)
    .head(10)
)

(
    GT(islands_mini)
    .tab_header(
        title="Large Landmasses of the World",
        subtitle="The top ten largest are presented"
    )
    .tab_stub(rowname_col="name")
    .tab_source_note(source_note="Source: The World Almanac and Book of Facts, 1975, page 406.")
    .tab_source_note(
        source_note=md("Reference: McNeil, D. R. (1977) *Interactive Data Analysis*. Wiley.")
    )
    .tab_stubhead(label="landmass")
    .fmt_integer(columns="size")
)