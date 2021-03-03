# Created by pyp2rpm-3.3.5
%global pypi_name typing

Name:           python-%{pypi_name}
Version:        3.7.4.3
Release:        1%{?dist}
Summary:        Type Hints for Python

License:        PSF
URL:            https://docs.python.org/3/library/typing.html
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Typing -- Type Hints for Python is a backport of the standard library
typing module to Python versions older than 3.5.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Typing -- Type Hints for Python is a backport of the standard library
typing module to Python versions older than 3.5.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 29 2021 Armando Neto <abiagion@redhat.com> - 3.7.4.3-1
- Initial package.
