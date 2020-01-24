version=$(python version.py);

if [ $? -ne 0 ]; then
    echo "Error getting current build version" >&2;

    exit 1;
fi

echo ::set-output name=version::$version