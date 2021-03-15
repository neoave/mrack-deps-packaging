# Created by pyp2rpm-3.3.5
%global pypi_name json-encoder

Name:           python-%{pypi_name}
Version:        0.4.4
Release:        1%{?dist}
Summary:        json encoder uses singledispatch pattern instead of JSONEncoder class overwrites

License:        None
URL:            None
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-pytest-runner
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(simplejson) >= 3.8.2
BuildRequires:  python3dist(six) >= 1.10

%description
json-encoder * json encoder uses singledispatch pattern_ instead of JSONEncoder
class overwrites.* No more *json.dumps(data, clsMyJSONEncoder)* everywhere.*
Comes with default serialization for time, date, datetime, UUID and Decimal*
Easy to use, easy to change serialization behaviour* Not tight to any json
implementation *json, simplejson, ujson* ...* It parse json float numbers into
Decimal...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(simplejson) >= 3.8.2
Requires:       python3dist(six) >= 1.10
%description -n python3-%{pypi_name}
json-encoder * json encoder uses singledispatch pattern_ instead of JSONEncoder
class overwrites.* No more *json.dumps(data, clsMyJSONEncoder)* everywhere.*
Comes with default serialization for time, date, datetime, UUID and Decimal*
Easy to use, easy to change serialization behaviour* Not tight to any json
implementation *json, simplejson, ujson* ...* It parse json float numbers into
Decimal...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/json_encoder
%{python3_sitelib}/json_encoder-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Mar 15 2021 Armando Neto <abiagion@redhat.com> - 0.4.4-1
- Initial package.
