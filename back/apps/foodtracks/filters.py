from django.contrib import admin


class ImportedRecordFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Record Imported'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'was_imported'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Yes', 'Importados'),
            ('No', 'Cargados por el usuario'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value
        # to decide how to filter the queryset.
        if self.value() == 'Yes':
            return queryset.filter(
                objectid__isnull=False,
            )

        if self.value() == 'No':
            return queryset.filter(
                objectid__isnull=True,
            )
