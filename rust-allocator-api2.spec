# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# FIXME tests fail in 0.2.18 (possibly just deps)
%bcond_with check
%global debug_package %{nil}

%global crate allocator-api2

Name:           rust-allocator-api2
Version:        0.2.18
Release:        1
Summary:        Mirror of Rust's allocator API
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/allocator-api2
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Mirror of Rust's allocator API.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(allocator-api2) = 0.2.18
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(allocator-api2/default) = 0.2.18
Requires:       cargo
Requires:       crate(allocator-api2) = 0.2.18
Requires:       crate(allocator-api2/std) = 0.2.18

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(allocator-api2/alloc) = 0.2.18
Requires:       cargo
Requires:       crate(allocator-api2) = 0.2.18

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(allocator-api2/nightly) = 0.2.18
Requires:       cargo
Requires:       crate(allocator-api2) = 0.2.18

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(allocator-api2/serde) = 0.2.18
Requires:       (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(allocator-api2) = 0.2.18

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(allocator-api2/std) = 0.2.18
Requires:       cargo
Requires:       crate(allocator-api2) = 0.2.18
Requires:       crate(allocator-api2/alloc) = 0.2.18

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
