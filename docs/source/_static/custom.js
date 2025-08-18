// For correct display of Pandas Styled tables
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('table[id^="T_"]').forEach(table => {
        table.classList.add('dataframe');
    });
    // Add Dataframe class for statsmodels tables
    document.querySelectorAll('table.simpletable').forEach(table => {
        table.classList.add('dataframe');
    });    
});